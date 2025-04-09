def sourcetemplate(url):
    def inner(**kwargs):
        copy_url = url
        if kwargs != {}:
            copy_url += "?"
            for item in sorted(kwargs.items()):
                copy_url += f"{item[0]}" + "=" + f"{item[1]}" + "&"
            copy_url = copy_url[:-1]
        return copy_url
    return inner

# TEST_4:
url = 'https://all_for_comfort_life.com'
load = sourcetemplate(url)
print(load(smartphone='iPhone', notebook='huawei', sale=True))

# TEST_5:
url = 'https://hide_and_seek.harvard'
load = sourcetemplate(url)
print(load(wizard='Dambldor', magic_wand='elderberry', thief='Volandemord'))