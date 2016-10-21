import numpy
class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
	    self.coordinates = numpy.array(coordinates)
            #self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
	    return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self,v):

	    return numpy.add(self.coordinates,v.coordinates)

    def minus(self,v):

	    return numpy.subtract(self.coordinates,v.coordinates)

    def times_scalar(self,c):
    	   return c * self.coordinates

    def magnitude(self,tolerance=1e-10):
	   return numpy.sqrt((self.coordinates*self.coordinates).sum()) < tolerance

    def normalized(self): 
	   try:
	   	mag = self.magnitude()
	   	return  self.times_scalar(1./mag) 
	   except ZeroDivisionError:
		  raise Exception('Cannot normalize the zero vector')
    def dot(self,v,tolerance=1e-10):
	    return numpy.dot(self.coordinates,v.coordinates) < tolerance

    def angle_with(self,v, in_degrees=False,tolerance=1e-10):

	    try:
	    	u1 = self.normalized()
	    	u2 = v.normalized()

		print u1
		print u2

		print u1.dot(u2)


	    	angle_in_radians = numpy.arccos(u1.dot(u2))

	    	if in_degrees:
		    return (angle_in_radians * 180 / numpy.pi) < tolerance
		else:
	            return angle_in_radians < tolerance

	    except Exception as e:
		    if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MESG:
			    raise Exception('Cannot Comput an angle with zero vector')
		    else:
			    raise e

    def is_orthogonal_to(self,v):
	    return abs(self.dot(v))

    def is_parallel_to(self,v):
	    return (self.is_zero() or
	            v.is_zero() or
		    self.angle_with(v) == 0 or
		    self.angle_with(v) == numpy.pi)

    def is_zero(self,tolerance=1e-10):
	    return self.magnitude() < tolerance

x = Vector([1.671,-1.012,-0.318])
y = Vector([1.671,-1.012,-0.318])

v1 = Vector([-0.221,7.437])
v2 = Vector([8.813,-1.331,-6.247])

v3 = Vector([5.581,-2.136])
v4 = Vector([1.996,3.108,-4.554])

v5 = Vector([7.887,4.138])
v6 = Vector([-8.802,6.776])

v7 = Vector([-5.955,-4.904,-1.874])
v8 = Vector([-4.496,-8.755,7.103])

v9  = Vector([3.183,-7.627])
v10 = Vector([-2.668,5.319])

v11 = Vector([7.35,0.221,5.188])
v12 = Vector([2.751,8.259,3.985])

v13 = Vector([-7.579,-7.880])
v14 = Vector([22.737,23.64])

v15 = Vector([2.118,4.827])
v16 = Vector([0,0])




#print x.plus(y)
#
#print x.times_scalar(7.41)

#print v1.magnitude()
#print v2.magnitude()

#print v3.normalized()
#print v4.normalized()

#print v5.dot(v6)
#print v7.dot(v8)

#print v9.angle_with(v10)
#
#print v11.angle_with(v12,True)

print v13.is_parallel_to(v14)
print v13.is_orthogonal_to(v14)

print v15.is_parallel_to(v16)
print v15.is_orthogonal_to(v16)
