import numpy as np
from anytree import Node, NodeMixin

import cifParsing as cPrs
from Matrix import matrices_new_extended as mat


def check_symmetries_in_cell(
    cell: np.ndarray[float], matrices: np.ndarray[float] = mat.all_matrices
) -> np.ndarray[bool]:
    # def func(cell: numpy2d_array(float),
    # matrices: numpy3d_array(int)) -> mask numpy1d_array(bool):
    """
    making all transformations of a cell
    bringing back the order inside each transformed cell
    checking if there are the same cells as original cell
    """
    transformed_points = cell @ matrices
    transformed_points_sorted = np.array(
        [np.unique(points, axis=0) for points in transformed_points]
    )
    return np.array(
        [np.array_equal(points, cell) for points in transformed_points_sorted]
    )


class ReducedCell(NodeMixin):
    def __init__(
        self,
        cell,
        cell_indexes,
        atoms_labels,
        parent=None,
        children=None,
    ):
        super().__init__()
        self.parent = parent
        if children:
            self.children = children

        self.cell = cell
        self.cell_indexes = cell_indexes
        self.atoms_labels = atoms_labels

        self.vacancies_indexes = None
        # np.append(parent.vacancies, vacs, axis=0)
        self.symmetries_indexes = []
        self.symmetry_mask_cell = check_symmetries_in_cell(self.cell)
        self.symmetry_labels_cell = output_symmetries(self.symmetry_mask_cell)
        self.reduced_cell, self.reduced_cell_indexes = Tree.reduce_cell_by_symmetry2(
            self.cell, self.cell_indexes, self.symmetry_mask_cell
        )


class ReducedCell2(Node):
    file = None
    full_cell = np.array([])
    base_type = ""
    size = 0
    vacancy_amount = 0
    vacancies = np.array([])

    symmetry_mask_full_cell = []
    symmetry_labels_full_cell = []
    atoms_labels = []
    matrixes_full_cell = []

    @classmethod
    def set_parameters(cls, file, /, size, vacs):
        cls.file = file
        cls.size = size
        cls.vacancy_amount = vacs

    @classmethod
    def initialize_parameters(cls):
        cls.full_cell, cls.base_type = CPRS.getSCell2(cls.file, cls.size)
        cls.full_cell_indexes = list(range(len(cls.full_cell)))
        cls.symmetry_mask_full_cell = check_syms_in_cell(cls.full_cell)
        cls.symmetry_labels_full_cell = output_symmetries(cls.symmetry_mask_full_cell)

    def __init__(self, parent, vacancy_index):
        super().__init__(parent)
        self.cell, vacs = makeCellWithVacancies(vacancy_index)
        self.vacancies = np.append(parent.vacancies, vacs, axis=0)
        self.parent_symmetries = parent.instance_symmetries
        self.instance_symmetries = []
        self.matrixes = []

    def __repr__(self):
        return f"""{self.cell=}\n{self.parent=}\n{self.children=}\n{ReducedCell.full_cell=}\n{ReducedCell.size=}\n"""

    @classmethod
    def __makeCellWithVacancies(cls, index):
        indexes = set(index)
        cellVac = []
        Vac = []
        for nr, p in enumerate(cls.full_cell):
            if nr not in indexes:
                cellVac.append(p)
            else:
                Vac.append(p)
        return np.array(cellVac), np.array(Vac)


class Tree:
    # symmetry_mask_full_cell = []
    # symmetry_labels_full_cell = []
    # atoms_labels = []
    how_many_times_matrices_have_to_be_applied = []

    def __init__(self, file: str, size: int, vacancy_amount: int = 0):
        self.file = file
        self.size = size
        self.vacancy_amount = vacancy_amount
        self.cell, self.atoms_labels, _, _, self.base_type = cPrs.get_super_cell(
            self.file, self.size
        )
        self.cell_indexes = np.arange(self.cell.shape[0])
        self.unchanged_cell_aka_root = ReducedCell(
            self.cell, self.cell_indexes, self.atoms_labels
        )

    def run(self, depth: int):
        return Tree.make_tree(self.unchanged_cell_aka_root, depth)

    @staticmethod
    def make_tree(parent: ReducedCell, depth: int):
        if depth:
            for vacancy in parent.reduced_cell:
                cell = Tree.make_cell_with_vacancies(parent, vacancy)
                child = ReducedCell(cell, [1, 2, 3], [16, 16, 16], parent=parent)
                Tree.make_tree(child, depth - 1)

    @staticmethod
    def _get_matrices_for_specific_point_group(mask_present_symmetries):
        present_operations = np.ma.masked_where(
            mask_present_symmetries, mat.all_operations
        ).compressed()

        mask_for_matrices = np.array(
            [np.full((3, 3), val) for val in mask_present_symmetries]
        )
        present_matrices = (
            np.ma.masked_where(mask_for_matrices, mat.all_matrices)
            .compressed()
            .reshape((-1, 3, 3))
        )

        return present_matrices, present_operations

    @staticmethod
    def reduce_cell_by_symmetry(cell, symmetries):
        matrices, operations = Tree._get_matrices_for_specific_point_group(symmetries)
        cell_dict = {tuple(point): i for i, point in enumerate(cell, 1)}
        for matrix, op in zip(matrices, operations):
            for base_point in cell:
                if cell_dict[tuple(base_point)]:
                    for point in Tree._get_all_transformed_points(
                        matrix, base_point
                    ):  # , op):
                        cell_dict[tuple(point)] = 0

        # reduced_cell, reduced_cell_indexes = \
        #     [el for el in
        #      zip(*((point, index) for point, index in cell_dict.items() if
        #            index))]
        reduced_cell, reduced_cell_indexes = zip(
            *((point, index) for point, index in cell_dict.items() if index)
        )
        reduced_cell, reduced_cell_indexes = np.array(reduced_cell), np.array(
            reduced_cell_indexes
        )
        reduced_cell_indexes -= 1
        return reduced_cell, reduced_cell_indexes

    @staticmethod
    def reduce_cell_by_symmetry2(cell, indexes, symmetries):
        matrices, operations = Tree._get_matrices_for_specific_point_group(symmetries)
        cell_dict = {tuple(point): i + 1 for i, point in zip(indexes, cell)}
        for matrix, op in zip(matrices, operations):
            for base_point in cell:
                if cell_dict[tuple(base_point)]:
                    for point in Tree._get_all_transformed_points(
                        matrix, base_point
                    ):  # , op):
                        cell_dict[tuple(point)] = 0

        reduced_cell, reduced_cell_indexes = zip(
            *((point, index) for point, index in cell_dict.items() if index)
        )
        reduced_cell = np.array(reduced_cell)
        reduced_cell_indexes = np.array(reduced_cell_indexes)
        reduced_cell_indexes -= 1

        return reduced_cell, reduced_cell_indexes

    # @staticmethod
    # def _compare_points(p1: np.ndarray, p2: np.ndarray) -> bool:
    #     for a, b in zip(p1, p2):
    #         if a != b:
    #             return False
    #     return True

    @staticmethod
    def _get_all_transformed_points(
        matrix: np.ndarray, base_point: np.ndarray
    ) -> np.ndarray:
        transformed_point = matrix @ base_point
        while not Tree._compare_points(transformed_point, base_point):
            yield transformed_point
            transformed_point = matrix @ transformed_point

    # @staticmethod
    # def _get_all_transformed_points(matrix,base_point, number_of_operations):
    #     transformed_point = matrix @ base_point
    #     yield transformed_point
    #     for _ in range(number_of_operations - 1):
    #         transformed_point = matrix @ transformed_point
    #         yield transformed_point

    @staticmethod
    def make_cell_with_vacancies(cell, index):
        indexes = set(index)
        cell_vac = []
        vac = []
        for nr, p, i, l in enumerate(
            zip(cell.cell, cell.cell_indexes, cell.atoms_labels)
        ):
            if nr not in indexes:
                cell_vac.append(p)
            else:
                vac.append(p)
        return np.array(cell_vac), np.array(vac)


def output_symmetries(symmetries):
    return np.ma.masked_where(~symmetries, mat.all_labels).compressed().tolist()


# check_anti_syms_in_cell
# True_syms
# get_matrices
# check_all_cells

if __name__ == "__main__":
    my_tree = Tree("cif files/ZnS-Sfaleryt.cif", size=2, vacancy_amount=2)


# root = ReducedCell("root")
# child_1_1 = ReducedCell("child_1_1")
# child_1_2 = ReducedCell("child_1_2")
# child_1_3 = ReducedCell("child_1_3")
# child_1_4 = ReducedCell("child_1_4")
#
# root.add_children([child_1_1, child_1_2, child_1_3, child_1_4])
#
# child_2_1 = ReducedCell("child_2_1")
# child_2_2 = ReducedCell("child_2_2")
# child_2_3 = ReducedCell("child_2_3")
#
# child_1_1.add_children([child_2_1, child_2_2])
# child_1_2.add_children([child_2_3])
#
# root.print_children()
