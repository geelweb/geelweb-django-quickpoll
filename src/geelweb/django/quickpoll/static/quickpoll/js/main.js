/**
 * license: MIT
 * author: Guillaume Luchet <guillaume@geelweb.org>
 */

requirejs.config({
    paths: {
        'jquery'        : 'lib/vendor/jquery',
        'jquery-ui'     : 'lib/vendor/jquery-ui',
        'backbone'      : 'lib/vendor/backbone',
        'underscore'    : 'lib/vendor/underscore',
        'poll'          : 'lib/model/poll',
        'question'      : 'lib/model/question',
    },
    shim: {
        'backbone'                  : {deps: ['jquery', 'underscore']},
        'jquery-ui'                 : {deps: ['jquery']},
        'poll'                      : {deps: ['backbone']},
        'lib/view/ribbon'           : {deps: ['backbone']},
        'lib/view/poll'             : {deps: ['backbone', 'jquery-ui']},
    },
    deps: [
        'underscore',
        'backbone',
    ],
});

define(function bootstrap(require) {
    $(function() {
        // Load the poll
        // TODO get the first available poll
        var PollModel = require('poll'),
            poll = new PollModel({id: 1});

        poll.fetch();

        // Load the poll view
        var PollView = require('lib/view/poll'),
            dialog = new PollView({
                'model': poll,
            });

        // Load the ribbon
        var RibbonView = require('lib/view/ribbon'),
            ribbon = new RibbonView({
                'dialog': dialog,
            });

        ribbon.render();
    });
});

