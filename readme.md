# Steam Formatter

This is WIP application!

The purpose of this little cli application is to convert reddit comments or game deals to markdown data.

    Usage: steamf [OPTIONS] URL

      Outputs markdown table of games found in online sources:  bundlestars.com
      bundle pages, reddit comments(permalink) or posts

    Options:
      --nolog                         produce no log
      --sort [name|rating|tags|steam_url]
                                      sort fields  [default: rating]
      --help                          Show this message and exit.

## Example

    $ steamf "https://www.bundlestars.com/en/bundle/killer-bundle-x"

results in:

    | Name   | Rating     | Tags   |
    |:-------|:----------:|:-------|
    |[SEUM: Speedrunners from Hell](http://store.steampowered.com/app/457210)  | 95%  | 3D Platformer,Parkour,First-Person  |
    |[Pang Adventures](http://store.steampowered.com/app/415150)  | 90%  | Action,Arcade,Retro  |
    |[Human: Fall Flat](http://store.steampowered.com/app/477160)  | 89%  | Indie,Funny,Physics  |
    |[Mainlining](http://store.steampowered.com/app/454950)  | 86%  | Indie,Adventure,Simulation  |
    |[Stronghold Legends: Steam Edition](http://store.steampowered.com/app/40980)  | 81%  | Strategy,Simulation,City Builder  |
    |[Aarklash: Legacy](http://store.steampowered.com/app/222640)  | 79%  | RPG,Strategy,Tactical  |
    |[The Flame in the Flood](http://store.steampowered.com/app/318600)  | 78%  | Survival,Adventure,Indie  |
    |[Monochroma](http://store.steampowered.com/app/265830)  | 77%  | Indie,Adventure,Action  |
    |[Warhammer 40,000: Regicide](http://store.steampowered.com/app/322910)  | 73%  | Warhammer 40K,Strategy,Chess  |
    |[VoidExpanse](http://store.steampowered.com/app/324260)  | 65%  | Space,RPG,Action  |
