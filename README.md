# Menu Builder
*Create and Manange simple and dynamic menues for your site.*

### Requirements
**Menu Builder** is developed and require Django>=1.9.


### Installation
It can be installed via pip running the next command.
```
pip install git+https://github.com/marsxn/menu-builder.git
```

After installation, you must include it in your ```settings.py```. You can add it via the app config file, or the appname. 

```
INSTALLED_APPS = [
    ...
    # MB config file
    'menubuilder.apps.MenubuilderConfig',
    ...
    # MB appname
    'menubuilder',
]
```

Finally, run the migration executing ```python manage.py migrate```

**Congrats, it's ready!***

### Using it

Once you have installed this package, you'll be able to create and manage new items from Django Admin site. Create your own menues and include those using the next Template Tag.

```
{% create_menu 'MENU_SLUG' %}
```
