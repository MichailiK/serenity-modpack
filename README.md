# Serenity Modpack

A Minecraft 1.20.1 Fabric modpack for the private Serenity SMP, making use of
[packwiz](https://github.com/packwiz/packwiz) for maintaining the modpack.

## Documentation

- [Mod Introductions](/docs/mod_introductions/) (Start here!)
- [Mod List](/docs/mod_list/)


## Modpack Developer Notes

This section is used to note any remarks or outstanding issues with this modpack
and its development.

### Creating a MultiMC instance out of the modpack

The steps are nearly identical as to
[packwiz's guide](https://packwiz.infra.link/tutorials/installing/packwiz-installer/#creating-a-multimc-instance-for-your-modpack),
the only difference is, before exporting the instance as a zip, copy everything
from the `profile_defaults` directory in this repository to the instance.
The folder contains some (config) files with sane defaults.

This approach allows us to provide users with sane default settings, without
packwiz indexing/tracking & overwriting these files, allowing users to change
them as they wish.

### External mods

Some mods had to be retrieved outside of Modrinth or Curseforge, and can thus
not auto-update:

- [Create: Interactive](https://modrinth.com/mod/interactive): Uses a patched
  version to work with Sodium. See also
  [Issue](https://github.com/ValkyrienSkies/Create-Interactive-Issues/issues/73).
- [Distant Horizons](https://modrinth.com/mod/distanthorizons): Uses
  [this nightly build](https://gitlab.com/jeseibel/distant-horizons/-/jobs/artifacts/main/download?job=build:%20[1.20.1])
  which is compatible with Iris.
- [Iris Flywheel Compat](https://modrinth.com/mod/iris-flw-compat): Uses
  a patched build which works with Iris 1.7.
- Valkyrien Skies: Massive MSPT spikes caused by a mixin, the patched version
  just removes the problematic mixin from the mixins.json file. See also
  [issue](https://github.com/ValkyrienSkies/Valkyrien-Skies-2/issues/806)