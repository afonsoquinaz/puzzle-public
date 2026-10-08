# Store assets

- `listing.md` — overview of the listing (name, category, price, subtitles and keywords).
- `metadata/` — upload-ready App Store text for the English storefronts in fastlane's
  `deliver` layout: `en-US`, `en-GB`, `en-AU`, `en-CA` (name, subtitle, keywords,
  promotional text, description, release notes, support / privacy / marketing URLs) plus
  the app-level category and copyright files. Check limits with
  `python3 store/check_metadata.py`, then upload text only with
  `fastlane deliver --app_identifier com.afonso.detour --metadata_path store/metadata --skip_binary_upload --skip_screenshots`
  (or paste each file into App Store Connect: add the language under App Information >
  Localizable Information, then fill the version page). The same screenshots serve all four.
- `iphone69_*.jpg` — 6.9" iPhone screenshots (1320×2868), real gameplay rendered headless
  with `dev/flow_probe.gd` in the game repo (no mock-ups). Order: first level, tank routes,
  tank smash, plates & gates, perfect clear, home + daily, levels.
- `../icon.png` — app icon (1024×1024, no alpha): a yellow DETOUR diamond with a bent arrow
  and a zombie on a curving road at dusk, rendered with the game's own models
  (`dev/icon_scene.gd` in the game repo).
