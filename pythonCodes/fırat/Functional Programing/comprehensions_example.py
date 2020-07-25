some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]


duplicates = list(
    set([item for item in some_list if some_list.count(item) > 1]))
print(duplicates)
# ilk önce list set e çevirilir çünkü set tekrarlara izin vermez sonra set tekrar liste çevirilir.
