'''
Generalized Rigid body motion integration functionality.
Main class (6Dof) is `MAPLEAF.Motion.RigidBody.RigidBody`.  
Fundamental data types used throughout the simulator defined in:

* `CythonVector.Vector`
* `CythonQuaternion.Quaternion` - represents orientation
* `CythonAngularVelocity.AngularVelocity` 
* `Inertia.Inertia` - stores component masses and moments of inertias
* `ForceMomentSystem.ForceMomentSystem`  - stores a repositionable force-moment system

3Dof and 6DoF Rigid body states are composed of these fundamental data types and defined in `RigidBodyStates`

Generalized constant and adaptive time stepping integrators are defined in `Integration`

.. image:: https://www.researchgate.net/profile/Alireza_Abbaspour2/publication/326452421/figure/fig1/AS:701040399753217@1544152464477/The-aircraft-coordinate-system-34.jpg
'''
# Make the classes in all submodules importable directly from MAPLEAF.Rocket
from .CythonVector import *
from .CythonQuaternion import *
from .CythonAngularVelocity import *
from .Interpolation import *
from .inertia import *
from .RigidBodyStates import *
from .RigidBodies import *

# For some reason CythonVector and company don't exist down here, so they won't import when running from MAPLEAF.Motion import *
subModules = [ inertia, RigidBodies, RigidBodyStates, Interpolation ]

__all__ = [ "Vector", "Quaternion", "AngularVelocity" ]

for subModule in subModules:
    __all__ += subModule.__all__