import inspect
from textwrap import dedent
from typing import Any, Callable, Set, Dict, get_type_hints


class IDE:
    def __init__(self, obj: Any):
        self.source_code_dict: Dict[type, str] = {}
        self.unread_types: Set[type] = set()
        self.collect_types_from_object(obj)

    def collect_types_from_object(self, obj: Any):
        annotations = set()
        if inspect.isclass(obj):
            annotations.update(get_type_hints(obj).values())
            for _, method in inspect.getmembers(obj, predicate=inspect.isfunction):
                method_annotations = get_type_hints(method)
                annotations.update(method_annotations.values())
        elif inspect.isfunction(obj):
            annotations.update(get_type_hints(obj).values())
        else:
            return

        for ann in annotations:
            for typ in self.get_all_types_from_annotation(ann):
                if isinstance(typ, type) and typ.__module__ != "builtins":
                    if typ not in self.source_code_dict:
                        self.unread_types.add(typ)

    def get_all_types_from_annotation(self, annotation: Any) -> Set[type]:
        types = set()
        if isinstance(annotation, type):
            types.add(annotation)
        elif hasattr(annotation, "__origin__") and hasattr(annotation, "__args__"):
            origin = annotation.__origin__
            args = annotation.__args__
            if isinstance(origin, type):
                types.add(origin)
            for arg in args:
                types.update(self.get_all_types_from_annotation(arg))
        return types

    def read_source(self, t: type, postprocessor: Callable[[str], str] | None = None):
        if t in self.source_code_dict:
            return self.source_code_dict[t]
        try:
            source = inspect.getsource(t)
            source = dedent(source)
            if postprocessor:
                source = postprocessor(source)
            self.source_code_dict[t] = source
            self.unread_types.discard(t)
            self.collect_types_from_object(t)
        except (TypeError, OSError):
            self.source_code_dict[t] = None
            self.unread_types.discard(t)

        return self.source_code_dict[t]
