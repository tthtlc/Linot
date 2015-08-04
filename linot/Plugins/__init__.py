import pkgutil
__all__ = []
List = {}
for loader, module_name, is_pkg in pkgutil.iter_modules(__path__):
    if is_pkg:
        __all__.append(module_name)
        module = loader.find_module(module_name).load_module(module_name)
        exec('%s = module' % module_name)
        __import__(module_name+'.Plugin')
        List[module_name] = module.Plugin
