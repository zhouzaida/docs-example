from typing import Optional, Union


class ClassDocstring:
    """Summarize the function of the class in one sentence.

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
    successfully.

    Note:
        If the class has something important to remind the user, we can show
        it in the note block.

    Warning:
        If the class has something important to warn the user, such as a change
        in the interface, we can show it in the warning block.

    Sometimes we want to use formulas to represent some definitions, we can
    write them within lines like :math:`e^{i \pi}+1=0`. Or we can write it
    between lines like::

    .. math::
        e^{i \pi}+1=0

    Note:
        Of course, we can also write the formula in block like
        :math:`e^{i \pi}+1=0` or the following format::

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
        arg1 (int): ``arg1`` is the first parameter.
        arg2 (str, optional): ``arg2`` is the second parameter. Defaults to
            None. Note that if the default value is None, then you need to add
            optional to the parameter type. If the description of a parameter
            is too long, just indent it with a new line.
        arg3 (str): Of course, We can list some optional values wit the
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
        Note that the usage of ``here``, `here`, and "here" are different.
        In reStructured syntax, ``here`` means a piece of code. `here` means
        italics. "here" has no special meaning, but can be used to represent a
        string. The usage of `here` is different from that in Markdown, so you
        should pay attention to it.
    """
    def __init__(self,
                 args1: int,
                 args2: Optional[str] = None,
                 args3: str = 'item1',
                 args4: Optional[dict] = None):
        pass

    def method1(self, arg1: int, arg2: Union[str, list], arg3: dict) -> str:
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
            str: Return the output.
        """
        return 'method1'
    
    def method2(self, arg1: int, arg2: Union[str, list], arg3: dict) -> dict:
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
