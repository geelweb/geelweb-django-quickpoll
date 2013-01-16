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
        'lib/collection/poll'       : {deps: ['backbone']},
    },
    deps: [
        'underscore',
        'backbone',
    ],
});

define(function bootstrap(require) {
    $(function () {
        // Load the polls collection
        var PollCollection = require('lib/collection/poll'),
            polls = new PollCollection();

        var scripts = $('script[data-main$="quickpoll/js/main.js"]'),
            script = scripts[0],
            ribbon_container = script.getAttribute('data-container'),
            ribbon_type = script.getAttribute('data-type'),
            ribbon_label = script.getAttribute('data-label');

        polls.fetch({
            success: function (collection, response, options) {
                // get the first poll
                var poll = collection.first(),

                    PollView = require('lib/view/poll'),
                    dialog = new PollView({
                        'model': poll,
                    }),

                    RibbonView = require('lib/view/ribbon'),
                    ribbon = new RibbonView({
                        'dialog': dialog,
                        'type': ribbon_type,
                        'container': ribbon_container,
                        'label': ribbon_label,
                    });

                // Load the ribbon
                ribbon.render();
            }
        });
    });
});

