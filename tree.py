class Node:
    def __init__(self, data, depth):
        self.left = None
        self.right = None
        self.center = None
        self.data = data
        self.depth = depth

    def insertLeft(self, data, depth):
        self.left = Node(data, depth)
        return self.left

    def insertRight(self, data, depth):
        self.right = Node(data, depth)
        return self.right

    def insertCenter(self, data, depth):
        self.center = Node(data, depth)
        return self.center

    def PrintTree(self):
        print("--" * self.depth, end="")
        print(self.data)
        if self.left:
            self.left.PrintTree()
        if self.center:
            self.center.PrintTree()
        if self.right:
            self.right.PrintTree()


# Build tree
root = Node(0, 0)
c01 = root.insertCenter(1, 1)
c02 = c01.insertCenter(2, 2)
c03 = c02.insertCenter(3, 3)
c04 = c03.insertCenter(4, 4)
c14 = c04.insertCenter(14, 5)
c13 = c14.insertRight(13, 6)
c15 = c14.insertLeft(15, 6)
c12 = c13.insertCenter(12, 7)
c23 = c13.insertLeft(23, 7)
c05 = c15.insertLeft(5, 7)
c16 = c15.insertCenter(16, 7)
c11 = c12.insertCenter(11, 8)
c22 = c23.insertRight(22, 8)
c24 = c23.insertLeft(24, 8)
c06 = c05.insertCenter(6, 8)
c26 = c16.insertCenter(26, 8)
c10 = c11.insertCenter(10, 9)
c21 = c11.insertLeft(21, 9)
c32 = c22.insertLeft(32, 9)
c25 = c24.insertCenter(25, 9)
c07 = c06.insertCenter(7, 9)
c27 = c26.insertLeft(27, 9)
c36 = c26.insertCenter(36, 9)
c20 = c10.insertLeft(20, 10)
c31 = c21.insertCenter(31, 10)
c42 = c32.insertCenter(42, 10)
c17 = c07.insertRight(17, 10)
c37 = c27.insertRight(37, 10)
c35 = c36.insertCenter(35, 10)
c30 = c20.insertCenter(30, 11)
c41 = c31.insertCenter(41, 11)
c52 = c42.insertCenter(52, 11)
c47 = c37.insertCenter(47, 11)
c40 = c41.insertRight(40, 12)
c51 = c41.insertCenter(51, 12)
c53 = c52.insertLeft(53, 12)
c57 = c47.insertCenter(57, 12)

# Path 2
c62p2 = c52.insertCenter(62, 12)
c50 = c51.insertRight(50, 13)
c54 = c53.insertCenter(54, 13)
c56 = c57.insertRight(56, 13)
c67 = c57.insertCenter(67, 13)
c63p2 = c62p2.insertLeft(63, 13)
c72p2 = c62p2.insertCenter(72, 13)
c60 = c50.insertLeft(60, 14)
c77 = c67.insertCenter(77, 14)
c64p2 = c63p2.insertCenter(64, 14)
c71p2 = c72p2.insertRight(71, 14)
c73p2 = c72p2.insertLeft(73, 14)
c61 = c60.insertLeft(61, 15)
c76 = c77.insertRight(76, 15)
c65p2 = c64p2.insertCenter(65, 15)
c70p2 = c71p2.insertCenter(70, 15)
c74p2 = c73p2.insertCenter(74, 15)

# Path 3
c66 = c76.insertRight(66, 16)
c62p3 = c61.insertCenter(62, 16)

# Path 2 continued
c55p2 = c65p2.insertLeft(55, 16)
c75p2 = c65p2.insertRight(75, 16)

# Path 1
c65p1 = c66.insertLeft(65, 17)

# Path 2 continued
c45p2 = c55p2.insertCenter(45, 17)

# Path 3
c63p3 = c62p3.insertCenter(63, 17)
c72p3 = c62p3.insertRight(72, 17)

# Path 1 continued
c55p1 = c65p1.insertRight(55, 18)
c75p1 = c65p1.insertLeft(75, 18)

# Path 2 continued
c44p2 = c45p2.insertLeft(44, 18)
c46p2 = c45p2.insertRight(46, 18)

# Path 3 continued
c64p3 = c63p3.insertCenter(64, 18)
c71p3 = c72p3.insertRight(71, 18)
c73p3 = c72p3.insertLeft(73, 18)

# Path 1 continued
c45p1 = c55p1.insertCenter(45, 19)

# Path 3 continued
c65p3 = c64p3.insertCenter(65, 19)
c70p3 = c71p3.insertCenter(70, 19)
c74p3 = c73p3.insertCenter(74, 19)

# Path 1 continued
c44p1 = c45p1.insertLeft(44, 20)
c46p1 = c45p1.insertRight(46, 20)

# Path 3 continued
c55p3 = c65p3.insertLeft(55, 20)
c75p3 = c65p3.insertRight(75, 20)

# Path 3 continued
c45p3 = c55p3.insertCenter(45, 21)

# Path 3 continued
c44p3 = c45p3.insertLeft(44, 22)
c46p3 = c45p3.insertRight(46, 22)

# Print the tree
root.PrintTree()
