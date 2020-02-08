# -*- mode: python -*-

import transmogrifier

CONFIG = transmogrifier.Config(
    build_dir = './build',
    repo = 'grandrapids',
    package_name = 'montclair-grandrapids',
    name = 'Go Grand Rapids',
    description = 'Real Time Tracking of the Buses for Grand Rapids, MI',
    url = 'https://grandrapids.gotransitapp.com',
    logo_svg = 'assets/logo.svg',
    montclair_config = transmogrifier.MontclairConfig(
        version = '1.6.4',
        revision = 1,
        title = 'Go Grand Rapids',
        first_run_text = "Welcome to Grand Rapids, MI's Real Time Bus Tracker.<br /><br />Please select one or more routes to begin!",
        configuration_js_file = 'assets/Configuration.js'
    ),
    ios_config = transmogrifier.MontclairiOSConfig(
        version = '2.0.5',
        revision = 1,
        app_id = 'com.gotransitapp.grandrapids',
        app_store_id = '1495117817',
        app_store_url = 'https://apps.apple.com/us/app/go-grand-rapids/id1495117817'
    ),
    android_config = transmogrifier.MontclairAndroidConfig(
        version = '1.0.2',
        revision = 1,
        app_id = 'com.gotransitapp.grandrapids',
        play_store_url = 'https://play.google.com/store/apps/details?id=com.gotransitapp.grandrapids'
    )
)
