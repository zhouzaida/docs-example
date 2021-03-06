# Modified from
# https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
"""Example Google style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html
"""

from typing import Optional, Union

module_level_variable1 = 12345
module_level_variable2 = 98765
"""int: Module level variable documented inline.

The docstring may span multiple lines. The type may optionally be specified
on the first line, separated by a colon.
"""


def module_level_function(param1, param2=None, *args, **kwargs):
    r"""This is an example of a module level function.

    Function parameters should be documented in the ``Args`` section. The name
    of each parameter is required. The type and description of each parameter
    is optional, but should be included if not obvious.

    If *args or **kwargs are accepted,
    they should be listed as ``*args`` and ``**kwargs``.

    The format for a parameter is::

        name (type): description
            The description may span multiple lines. Following
            lines should be indented. The "(type)" is optional.

            Multiple paragraphs are supported in parameter
            descriptions.

    Args:
        param1 (int): The first parameter.
        param2 (:obj:`str`, optional): The second parameter. Defaults to None.
            Second line of description should be indented.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        bool: True if successful, False otherwise.

        The return type is optional and may be specified at the beginning of
        the ``Returns`` section followed by a colon.

        The ``Returns`` section may span multiple lines and paragraphs.
        Following lines should be indented to match the first line.

        The ``Returns`` section supports any reStructuredText formatting,
        including literal blocks::

            {
                'param1': param1,
                'param2': param2
            }

    Raises:
        AttributeError: The ``Raises`` section is a list of all exceptions
            that are relevant to the interface.
        ValueError: If `param2` is equal to `param1`.
    """
    if param1 == param2:
        raise ValueError('param1 may not be equal to param2')
    return True


def example_generator(n):
    """Generators have a ``Yields`` section instead of a ``Returns`` section.

    Args:
        n (int): The upper limit of the range to generate, from 0 to `n` - 1.

    Yields:
        int: The next number in the range of 0 to `n` - 1.

    Examples:
        Examples should be written in doctest format, and should illustrate how
        to use the function.

        >>> print([i for i in example_generator(4)])
        [0, 1, 2, 3]
    """
    yield from range(n)


class ExampleClass:
    r"""The summary line for a class docstring should fit on one line.

    Describe the function of the class in a few sentences, including but not
    limited to what the class is and what it can do.

    In the docstring, we can list some items with the following format:

    - item1
    - item2
    - item3
    - item4

    If we want to quote a URL, then we can quote it like
    `OpenMMLab <https://github.com/open-mmlab>`_. Note that there needs to be a
    space between the title and the link, otherwise it will not render
    successfully. We can also quota a link like `OpenMMLab`_.

    Note:
        If the class has something important to remind the user, we can show
        it in the note block.

    Warning:
        If the class has something important to warn the user, such as a change
        in the interface, we can show it in the warning block.

    Sometimes we want to use formulas to represent some definitions, we can
    write them within lines like :math:`e^{i \pi}+1=0`. Or we can write it
    between lines like.

    .. math::
        e^{i \pi}+1=0

    Note:
        Of course, we can also write the formula in block like
        :math:`e^{i \pi}+1=0` or the following format.

        .. math::
            e^{i \pi}+1=0

    To make it easier for users to get started quickly, we can give some
    introductory examples in the example block.

    Examples:
        >>> # initialization
        >>> obj = ClassDocstring(1)
        >>> # give a few more examples
        >>> obj = ClassDocstring(1, 'second parameter')

    Args:
        arg1 (int): ``arg1`` is the first parameter. If we want to quote a link
            to explain the argument, we can say that see more details at
            `website`_.
        arg2 (str, optional): ``arg2`` is the second parameter. Defaults to
            None. Note that if the default value is None, then you need to add
            optional to the parameter type. If the description of a parameter
            is too long, just indent it with a new line.
        arg3 (str): Of course, We can list some optional values with the
            following format. Defaults to ``item1``.

            - item1
            - item2. If the description of a parameter is too long, just indent
              it with a new line. Be careful to the indentation alignment
              between lines otherwise there will be unexpected rendering
              result.
        arg4 (dict, optional): If the parameter is a dictionary, we can
            describe it with the following format. Defaults to None.

            - key1: This is a shot description of the item.
            - key1: This is a shot description of the item.

    Note:
        Properties created with the ``@property`` decorator should be
        documented in the property's getter method.

    Note:
        Note that the usage of ``double backticks``, `single backticks`, and
        "double quotation marks" are different. In reStructured syntax,
        ``double backticks`` means a piece of code. `single backticks` means
        italics. "double quotation marks" has no special meaning, but can be
        used to represent a string. The usage of `single backticks` is
        different from that in Markdown, so you should pay attention to it.

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below). Note
    that the ``Attributes`` section is optional.

    Attributes:
        args1 (int): Description of `args1`.
        args2 (:obj:`str`, optional): Description of `args2`.

    .. _OpenMMLab:
        https://github.com/open-mmlab
    .. _website:
        https://openmmlab.com/
    """
    def __init__(self,
                 arg1: int,
                 arg2: Optional[str] = None,
                 arg3: str = 'item1',
                 arg4: Optional[dict] = None):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3  #: Doc comment *inline* with attribute
        #: dict or None: Doc comment *before* attribute, with type specified
        self.arg4 = arg4
        self._class_name = 'ExampleClass'
        self._owner = 'OpenMMLab'

    @property
    def class_name(self):
        """str: Properties should be documented in their getter method."""
        return self._class_name

    @property
    def owner(self):
        """:obj:`str`: Properties with both a getter and setter should only be
        documented in their getter method. If the setter method contains
        notable behavior, it should be mentioned here.
        """
        return self._owner

    @owner.setter
    def owner(self, new_owner):
        self._owner = new_owner

    def __special__(self):
        """By default special members with docstrings are not included.

        Special members are any methods or attributes that start with and
        end with a double underscore. Any special member with a docstring
        will be included in the output, if
        ``napoleon_include_special_with_doc`` is set to True.

        This behavior can be enabled by changing the following setting in
        Sphinx's conf.py::

            napoleon_include_special_with_doc = True
        """
        pass

    def _private(self):
        """By default private members are not included.

        Private members are any methods or attributes that start with an
        underscore and are *not* special. By default they are not included
        in the output.

        This behavior can be changed such that private members *are* included
        by changing the following setting in Sphinx's conf.py::

            napoleon_include_private_with_doc = True
        """
        pass

    def return_string(self, arg1: int, arg2: Union[str, list],
                      arg3: dict) -> str:
        """Summarize the function of the method in one sentence.

        Describe the function of the class in a few sentences. Of course,
        it is not required.

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            arg1 (int): ``arg1`` is the first parameter.
            arg2 (str | list): ``arg2`` is the second parameter. This parameter
                may be of type string or list.
            arg3 (dict): We can describe the parameter with the following
                format.

                - key1: This is a shot description of the item.
                - key1: This is a shot description of the item.

        Returns:
            str: Return the output.
        """
        return 'method1'

    def return_dict(self, arg1: int, arg2: Union[str, list],
                    arg3: dict) -> dict:
        """Summarize the function of the method in one sentence.

        Describe the function of the class in a few sentences. Of course,
        it is not required.

        Args:
            arg1 (int): ``arg1`` is the first parameter.
            arg2 (str | list): ``arg2`` is the second parameter. This parameter
                may be of type string or list.
            arg3 (dict): We can describe the parameter with the following
                format.

                - key1: This is a shot description of the item.
                - key1: This is a shot description of the item.

        Returns:
            dict: Return the output where the keys denote A meaning and values
            denote B. Be careful to the indentation alignment between lines
            otherwise there will be unexpected rendering result.
        """
        return {'key1': 'value1', 'key2': 'value2'}

    def return_tuple(self) -> tuple:
        """Return a tuple.

        Returns:
            tuple: Returns a tuple (a, b), where a is xxx, and b is xxx.
        """
        return (1, 2)

    def argument_list_changed(self, arg1: int, arg2: str = '') -> None:
        """If the argument list of a method have changed, we need to reflect
        that in the docstring.

        Note:
            More specifically, if the parameter is newly added, we can use the
            `New in version 1.1.1.` which `1.1.1` is the version parameter was
            added. If the meaning of the parameter are changed, we can use the
            `Changed in version 1.1.1.`.

        Warning:
            If the parameter was renamed, we need to tell user the interface
            was changed in the warning block.

        Args:
            arg1 (int): ``arg1`` is the first parameter.
            arg2 (str): ``arg2`` is the second parameter. Defaults to ''.
                `New in version 1.1.1.`
        """
        pass
