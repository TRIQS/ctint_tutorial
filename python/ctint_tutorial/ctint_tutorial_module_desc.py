# Generated automatically using the command :
# c++2py ../../c++/ctint_tutorial/ctint_tutorial.hpp -p --members_read_only -N ctint_tutorial -a ctint_tutorial -m ctint_tutorial_module -o ctint_tutorial_module --moduledoc="The ctint_tutorial python module" -C pytriqs --cxxflags="-std=c++17" --target_file_only
from cpp2py.wrap_generator import *

# The module
module = module_(full_name = "ctint_tutorial_module", doc = r"The ctint_tutorial python module", app_name = "ctint_tutorial")

# Imports

# Add here all includes
module.add_include("ctint_tutorial/ctint_tutorial.hpp")

# Add here anything to add in the C++ code at the start, e.g. namespace using
module.add_preamble("""
#include <cpp2py/converters/string.hpp>
#include <triqs/cpp2py_converters/h5.hpp>

using namespace ctint_tutorial;
""")


# The class toto
c = class_(
        py_type = "Toto",  # name of the python class
        c_type = "ctint_tutorial::toto",   # name of the C++ class
        doc = r"""A very useful and important class""",   # doc of the C++ class
        hdf5 = True,
        arithmetic = ("add_only"),
        comparisons = "==",
        serializable = "tuple"
)

c.add_constructor("""()""", doc = r"""""")

c.add_constructor("""(int i_)""", doc = r"""Construct from integer

Parameters
----------
i_
     a scalar  :math:`G(\tau)`""")

c.add_method("""int f (int u)""",
             doc = r"""A simple function with :math:`G(\tau)`

Parameters
----------
u
     Nothing useful""")

c.add_method("""std::string hdf5_scheme ()""",
             is_static = True,
             doc = r"""HDF5""")

c.add_property(name = "i",
               getter = cfunction("int get_i ()"),
               doc = r"""Simple accessor""")

module.add_class(c)

module.add_function ("int ctint_tutorial::chain (int i, int j)", doc = r"""Chain digits of two integers

Parameters
----------
i
     The first integer

j
     The second integer

Returns
-------
out
     An integer containing the digits of both i and j""")



module.generate_code()
