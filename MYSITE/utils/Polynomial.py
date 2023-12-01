class polynomialnode:
    def __init__(self, degree=None, coefficient=None):
        self.degree = degree
        self.coefficient = coefficient
        self.next = None


class polynomial:
    def __init__(self, degree, coefficient):
        if degree is None:
            self._polyhead = None

        else:
            self._polyhead = polynomialnode(degree, coefficient)
        self._polytail = self._polyhead

    def degree(self):
        """
        Gives the highest degree of the polynomial.
        """
        if self._polyhead is None:
            return -1

        else:
            return self._polyhead.degree

    def __getitem__(self, degree):
        """
        Gives the polynomial term having the degree mentioned by user.

        TEST CONDITIONS:
        1. If the degree is None.
        2. If the degree is present in the polynomial.
        3. If the degree is not present in the polynomial.
        """
        curNode = self._polyhead
        while curNode is not None and curNode.degree >= degree:
            curNode = curNode.next

        if curNode is None or curNode.degree != degree:
            return 0.0

        else:
            return curNode.degree

    def __addnode__(self, degree, coefficient):
        """
        Function to Add more values in the expression.
        :param degree: degree of the term.
        :param coefficient: coefficient of the term.

        TEST CONDITIONS:
        1. If the term is already present in the list.
        2. If the term is not present in the list.
        """

        newNode = polynomialnode(degree, coefficient)
        curNode = self._polyhead
        prevNode = None

        while curNode is not None and curNode.degree >= degree:
            prevNode = curNode
            curNode = curNode.next

        # If the node already contains same degree.
        if prevNode is not None and prevNode.degree == degree:
            prevNode.coefficient = prevNode.coefficient + coefficient

        else:
            prevNode.next = newNode

    def __remove__(self, degree, coefficient):
        """
        Function to remove a term from the polynomial expression.

        TEST CONDITIONS:
        1. If the term is not present in the expression.
        2. If the term is present in the expression.
        3. If an invalid term is entered.
        """

        target = polynomialnode(degree, coefficient)
        prevNode = None
        curNode = self._polyhead

        while curNode is not None and (curNode.degree != target.degree or curNode.coefficient != target.coefficient):
            prevNode = curNode
            curNode = curNode.next

        if curNode is not None:
            if curNode == self._polyhead:
                self._polyhead = curNode.next
            else:
                prevNode.next = curNode.next

    def addtwopolys(self, otherpoly):
        """
        Function which adds two one polynomial expression with other polynomial expression.
        :param otherpoly: other polynomial expression.
        :return: Nothing, but changes the original expression.

        TEST CONDITIONS:
        1. If the two polynomials have the same number of terms.
        2. If the two polynomials have different number of terms.
        """
        newpoly = polynomial(None, None)
        nodeA = self._polyhead
        nodeB = otherpoly._polyhead

        while nodeA is not None and nodeB is not None:

            # Switching nodes if one is greater than the other.
            if nodeA.degree > nodeB.degree:
                degree = nodeA.degree
                value = nodeA.coefficient
                nodeA = nodeA.next
                # print(degree)
                newpoly._appendterm(degree, value)

            elif nodeB.degree > nodeA.degree:
                degree = nodeB.degree
                value = nodeB.coefficient
                nodeB = nodeB.next
                # print(degree,'b')
                newpoly._appendterm(degree, value)

            else:
                degree = nodeA.degree
                otherpoly = nodeA.coefficient + nodeB.coefficient

                nodeA = nodeA.next
                nodeB = nodeB.next

            newpoly._appendterm(degree, otherpoly)

        while nodeA is not None:
            newpoly._appendterm(nodeA.degree, nodeA.coefficient)
            nodeA = nodeA.next

        while nodeB is not None:
            newpoly._appendterm(nodeB.degree, nodeB.coefficient)
            nodeB = nodeB.next

        return newpoly

    def subtracttwopolys(self, otherpoly):
        """
        Function which subtracts two one polynomial expression with other polynomial expression.
        :param otherpoly: other polynomial expression.
        :return: Nothing, but changes the original expression.

        TEST CONDITIONS:
        1. If the two polynomials have the same number of terms.
        2. If the two polynomials have different number of terms.
        """

        newpoly = polynomial(None, None)
        nodeA = self._polyhead
        nodeB = otherpoly._polyhead

        while nodeA is not None and nodeB is not None:

            # Switching nodes if one is greater than the other.
            if nodeA.degree > nodeB.degree:
                degree = nodeA.degree
                value = nodeA.coefficient
                nodeA = nodeA.next

            if nodeB.degree > nodeA.degree:
                degree = nodeB.degree
                value = nodeB.coefficient
                nodeB = nodeB.next

            else:
                degree = nodeA.degree
                otherpoly = nodeA.coefficient - nodeB.coefficient

                nodeA = nodeA.next
                nodeB = nodeB.next

            newpoly._appendterm(degree, otherpoly)

        while nodeA is not None:
            newpoly._appendterm(nodeA.degree, nodeA.coefficient)
            nodeA = nodeA.next

        while nodeB is not None:
            newpoly._appendterm(nodeB.degree, nodeB.coefficient)
            nodeB = nodeB.next

        return newpoly

    def multiplypolys(self, otherpoly):
        """
        Function which multiplies one polynomial expression with another polynomial expression.
        After that, it performs all the necessary addition or subtraction.
        :param otherpoly: other polynomial expression.
        :return: A multiplied expression.

        TEST CONDITIONS:
        1. If the two polynomials have the same number of terms.
        2. If the two polynomials have different number of terms.
        """

        newpoly = polynomial(0, 0)
        nodeA = self._polyhead
        nodeB = otherpoly._polyhead
        res_degree = None
        res_cof = None

        # Looping on the first polynomial.
        while nodeA is not None:
            nodeB = otherpoly._polyhead
            # Looping on the second polynomial.
            while nodeB is not None:
                res_cof = nodeA.coefficient * nodeB.coefficient
                res_degree = nodeA.degree + nodeB.degree
                nodeB = nodeB.next
                # Appending the result of multiplication with each term in a new polynomial expression.
                newpoly._appendterm(res_degree, res_cof)

            nodeA = nodeA.next

        # print(newpoly.display())          # Uncomment to check the new polynomial after multiplication.

        # Evaluating the answer by perform required addition/ subtraction.

        res_poly = polynomial(0, 0)
        curNodeA = newpoly._polyhead.next

        while curNodeA is not None:
            curNodeB = curNodeA.next
            res_cof = curNodeA.coefficient

            while curNodeB is not None:
                if curNodeA.degree == curNodeB.degree:
                    res_cof += curNodeB.coefficient
                    newpoly.__remove__(curNodeB.degree, curNodeB.coefficient)
                    curNodeB = curNodeB.next

                else:
                    curNodeB = curNodeB.next

            res_poly._appendterm(curNodeA.degree, res_cof)
            curNodeA = curNodeA.next
        res_poly.__remove__(0, 0)
        return res_poly

    def _appendterm(self, degree, coefficient):

        if coefficient != 0.0:
            newterm = polynomialnode(degree, coefficient)

            if self._polyhead is None:
                self._polyhead = newterm

            else:
                self._polytail.next = newterm

            self._polytail = newterm

    def display(self):
        from .externals.externals import sups
        # from MYSITE.MYSITE.utils.externals.externals import sups
        var = ''
        if (self._polyhead == None):
            # print("Polynomial is empty ")
            var = '0'
        curNode = self._polyhead
        while (curNode != None):
            if (curNode != self._polyhead):
                if curNode.coefficient > 0:
                    var += "+" + str(curNode.coefficient)
                    # print("+", curNode.coefficient, end="")
                else:
                    # print("-", abs(curNode.coefficient), end="")
                    var += "-" + str(abs(curNode.coefficient))
            else:
                var += str(curNode.coefficient)
                # print(curNode.coefficient, end="")

            if (curNode.degree != 0):
                var += sups('x', str(curNode.degree))
                # print(sups('x', str(curNode.degree)), end=" ", sep="")

            if curNode.next is None:
                break
            else:
                curNode = curNode.next
        return var


# noinspection PyBroadException
def make_polynomial(expression):
    """
    Function to take an expression from user and make out a polynomial of it using the linked list structure.

    TEST CASES:
    Test Cases that tells how a user may enter inputs:
    The user may use any variable for their equation.
    a)	ax^2 +/- bx +/- c = 0.
    b)	More terms…ax^3 +/- bx^2 +/- cx +/- d = 0.
    c)	…ax^3 +/- cx +/- d = 0.
    d)	…ax^2 +/- bx^3 +/- cx +/- d = 0.
    e)	…ax^3 +/- bx^2 +/- cx +/- d.
    f)	…ax^3 +/- cx +/- d = 0
    g)	…ax^3 +/- bx^2 +/- bx^2 +/- cx +/- d.

    :param expression: The input expression user will enter.
    :return: A polynomial object made out of that expression.
    """
    try:
        from .externals.externals import dict2
        # from MYSITE.MYSITE.utils.externals.externals import dict2
        import re

        # Replacing all variables with x.
        for i in expression:
            if i.isalpha():
                expression = expression.replace(i, 'x')

        # Splitting up the terms and operators.
        ex_terms = re.split('[+-]', expression)
        operators = re.findall('[+-]', expression)

        terms = []
        # Removing extra spaces in the terms.
        for i in range(len(ex_terms)):
            temp = ex_terms[i].strip()
            terms.append(temp.split('x'))

        len_op = len(operators)
        len_terms = len(terms)

        # Working for the condition when first term is negative.(It'll be empty since split from -ve sign.)
        if len_terms > len_op and terms[0][0] != '':
            operators = ['+'] + operators
        else:
            # Popping the first (empty) term.
            len_terms -= 1
            terms.pop(0)
            terms[0][0] = '-' + terms[0][0]

        # print(terms,operators)
        res_poly = polynomial(int(dict2[terms[0][1]]), int(terms[0][0]))

        for i in range(len_terms - 1):

            if operators[i] == '-':
                terms[i][0] = -1 * int((terms[i][0]))


        for i in range(1, len_terms):
            if terms[i][1] == '':
                terms[i][1] = '¹'
            if len(terms[-1]) == 1:
                terms[-1] = [terms[-1][0], '⁰']

            res_poly.__addnode__(int(dict2[terms[i][1]]), int(terms[i][0]))

        return res_poly

    except Exception:
        return None

# P1 = make_polynomial('2x⁴-3x³+1')
# P2 = make_polynomial('2x⁴-3x³+1')
# print(P1.display(),P2.display())
# print(P1.addtwopolys(P2).display())

# P3 = polynomial(2,3)
#
# P3.__addnode__(0,1)
#
# P4 = polynomial(2,5)
# P4.__addnode__(1,4)
# P4.__addnode__(0,1)
# print(P3.display(),P4.display())
# print(P3.addtwopolys(P4).display())
