/* -*- Mode: rjsx -*- */

/*******************************************
 * Copyright (2018)
 *  Marcus Dillavou <line72@line72.net>
 *  http://line72.net
 *
 * Montclair:
 *  https://github.com/line72/montclair
 *  https://montclair.line72.net
 *
 * Licensed Under the GPLv3
 *******************************************/

import AvailtecParser from './AvailtecParser';

class Configuration {
    constructor() {
        // Grand Rapids, MI
        this.center = [42.967101, -85.671030];
        this.tileserver = {
            url: 'https://grandrapids.gotransitapp.com/tiles/{z}/{x}/{y}.png',
            subdomains: ''
        };

        this.agencies = [
            {
                name: 'Routes',
                parser: new AvailtecParser('https://grandrapids.gotransitapp.com/api/no.php/InfoPoint')
            }
        ];
    }
}

export default Configuration;
