from matrix import *
from vector import *
from rational import *

def tests( ) :
    
    matrix1 = Matrix( Rational( 1, 2 ), Rational( 1, 3 ), Rational( -2, 7 ), Rational( 2, 8 ) )
    matrix2 = Matrix( Rational( -1, 3 ), Rational( 2, 7 ), Rational( 2, 5 ), Rational( -1, 7 ) )
    matrix3 = Matrix( Rational( 2, 3 ), Rational( -1, 4 ), Rational( 8, -3 ), Rational( 5, 6 ) )

    #task1
    print( "Test1. Compute the product of: " )
    print( "{}       x\n{}".format( matrix1, matrix2 ) )
    print( "The result is: \n{}".format( matrix1 @ matrix2 ) )

    #task2
    print( "Test2. Compute the inverse of: " )
    print( "{}".format( matrix1 ) )
    print( "The result is: \n{}".format( matrix1.inverse() ) )

    #task3a
    print( "Test3a. Verify associativity of matrix multiplication of: " )
    mul1 = ( matrix1 @ matrix2 ) @ matrix3
    mul2 = matrix1 @ ( matrix2 @ matrix3 )
    
    if mul1 == mul2 :
        
        print( "m1 is: \n{} \nm2 is: \n{} \nm3 is: \n{}".format( matrix1, matrix2, matrix3 ) )
        print( "Matrix multiplication is associative:\n( m1 x m2 ) x m3 = m1 x ( m2 x m3 )\n" )
    
    else :
        raise ValueError( "Associativity of multiplication is not valid!\n" )
    
    #task3b
    print( "Test3b. Verify distributivity of matrix multiplication with addition of: " )
    LHS1 = matrix1 @ ( matrix2 + matrix3 )
    RHS1 = ( matrix1 @ matrix2 ) + ( matrix1 @ matrix3 )
    LHS2 = ( matrix1 + matrix2 ) @ matrix3
    RHS2 = ( matrix1 @ matrix3 ) + ( matrix2 @ matrix3 )

    if LHS1 == RHS1 and LHS2 == RHS2 :
        
        print( "m1 is: \n{} \nm2 is: \n{} \nm3 is \n{}".format( matrix1, matrix2, matrix3 ) )
        print( "Matrix multiplication with addition is distributive: \nm1 x( m2 + m3 ) = m1 x m2 + m1 x m3 and ( m1 + m2 ) x m3 = m1 x m3 + m2 x m3\n" )

    else :
        raise ValueError( "Distributivity of multiplication is not valid!" )

    #task3c
    print( "Test3c. Verify correspondence of matrix multiplication to composition of application of: " )
    vector = Vector( 3, 5 )

    if matrix1( matrix2( vector ) ) == ( matrix1 @ matrix2 )( vector ) :
        
        print( "m1 is: \n{} \nm2 is: \n{} \nv is: \n{}\n".format( matrix1, matrix2, vector ) )
        print( "Matrix multiplication corresponds to composition of application:\nm1( m2( v ) ) = ( m1 x m2 )( v )\n" )

    else :
        raise ValueError( "Matrix multiplication does not correspond to composition of application" )

    #task3d
    print( "Test3d. Verify that determinant commutes over multiplication of:" )
    det1 = matrix1.determinant() * matrix2.determinant()
    det2 = ( matrix1 @ matrix2 ).determinant()

    if det1 == det2 :
        
        print( "m1 is: \n{} \nm2 is: \n{}".format( matrix1, matrix2 ) )
        print( "Determinant commutes over multiplication:\ndet( m1 ) x det( m2 ) = det( m1 x m2 )\n" )

    else :
        raise ValueError( "Determinant does not commute over multiplication!" )


    #task4
    print( "Test4. Verify that inverse of matrix is indeed its inverse of: " )
    identityM = Matrix( 1, 0, 0, 1 )
    res1 = matrix1 @ matrix1.inverse()
    res2 = matrix1.inverse() @ matrix1

    if res1 == identityM and res2 == identityM :
        
        print( "m1 is: \n{}".format( matrix1 ) )
        print( "The matrix and its inverse are correct:\nm1 x inv( m1 ) = I and inv( m1 ) x m1 = I" )

    else :
        raise ValueError( "Inverse of matrix is not its inverse!" )









def intersect( it1, it2 ):
    while True:
        v1 = next(it1)
        v2 = next(it2)

        if v1 < v2:
            v1 = next(it1)
        elif v1 > v2:
            v2 = next(it2)
        else:
            yield v1
            v1 = next(it1)
            v2 = next(it2)

