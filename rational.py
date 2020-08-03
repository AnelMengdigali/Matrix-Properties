from numbers import *

class Rational( Number ) :

    def __init__( self, num, denom = 1 ) :
        
        self.num = num
        self.denom = denom
        
        self.normalize( )

    def normalize( self ) :
        
        if ( self.denom < 0 ) :
            
            self.num = - self.num
            self.denom = - self.denom
        
        if( self.denom == 0 ) :
            raise ValueError( "The denominator is zero" )
        
        gcdValue = gcd( self.num, self.denom )
      
        self.num = self.num // gcdValue
        self.denom = self.denom // gcdValue
    
    def __repr__( self ) :
        
        if self.denom == 1 :
            return "{}". format( self.num )
        
        else :
            return "{} / {} ". format( self.num, self.denom )

    def __neg__( self ) :
        
        return Rational( - self.num, self.denom )
  
    def __add__( self, other ) :
        
        if not isinstance( other, Rational ):
            return Rational( self.num + ( self.denom * other ), self.denom )
        
        else:
            return Rational( ( self.num * other.denom ) + ( other.num * self.denom ), self.denom * other.denom )

    def __sub__( self, other ) :
        
        if not isinstance( other, Rational ):
            return Rational( self.num - ( self.denom * other ), self.denom )
        
        else:
            return Rational( ( self.num * other.denom ) - ( other.num * self.denom ), self.denom * other.denom )

    def __radd__( self, other ) :
        
        return self.__add__( other )
    
    def __rsub__( self, other ) :
        
        if not isinstance( other, Rational ):
            return Rational( ( self.denom * other ) - self.num , self.denom )
        
        else:
            return Rational( ( other.num * self.denom ) - ( self.num * other.denom ), self.denom * other.denom )

    def __mul__( self, other ) :
        
        if not isinstance( other, Rational ) :
            return Rational( other * self.num, self.denom )
        
        else :
            return Rational( self.num * other.num, self.denom * other.denom )

    def __truediv__( self, other ) :
        
        if not isinstance( other, Rational ) :
            return Rational( self.num, other * self.denom )
        
        else :
            return Rational( self.num * other.denom, self.denom * other.num )

    def __rmul__( self, other ) :
        
        return self.__mul__( other )
    
    def __rtruediv__( self, other ) :
        
        if not isinstance( other, Rational ) :
            return Rational( other * self.denom, self.num )
        
        else :
            return Rational( self.denom * other.num, self.num * other.denom )

    def __eq__( self, other ) :
        
        if not isinstance( other, Rational ) :
            other = Rational( other )

        return ( self.num == other.num and self.denom == other.denom )

    def __ne__( self, other ) :
        
        if not isinstance( other, Rational ) :
            other = Rational( other )
        
        return ( self.num != other.num or self.denom != other.denom )

    def __lt__( self, other ) :
        
        if not isinstance( other, Rational ) :
            other = Rational( other )
        
        product1 = self.num * other.denom
        product2 = other.num * self.denom
        
        return ( product1 < product2 )

    def __gt__( self, other ) :
        
        if not isinstance( other, Rational ) :
            other = Rational( other )

        product1 = self.num * other.denom
        product2 = other.num * self.denom
        
        return ( product1 > product2 )
            
    def __le__( self, other ) :
        
        if not isinstance( other, Rational ) :
            other = Rational( other )

        product1 = self.num * other.denom
        product2 = other.num * self.denom

        return ( product1 < product2 or product1 == product2 )

    def __ge__( self, other ) :
        
        if not isinstance( other, Rational ) :
            other = Rational( other )

        product1 = self.num * other.denom
        product2 = other.num * self.denom
        
        return ( product1 > product2 or product1 == product2 )

def gcd( n1, n2 ) :
    
    if n1 == 0 and n2 == 0 :
        raise ArithmeticError( "gcd(0,0) does not exist" )

    while n2:
        n1, n2 = n2, n1 % n2

    return abs( n1 )



    
   

    
    

    

