/**
 * license: MIT
 * author: Guillaume Luchet <guillaume@geelweb.org>
 */

define(function (require) {
    var model = require('lib/model/poll');

    return Backbone.Collection.extend({
        model: model,

        url: function () {
            return '/quickpoll/rest/polls';
        },
    });
});

