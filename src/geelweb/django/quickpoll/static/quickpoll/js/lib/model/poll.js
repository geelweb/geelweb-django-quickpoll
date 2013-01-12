/**
 * license: MIT
 * author: Guillaume Luchet <guillaume@geelweb.org>
 */

define(function (require) {
    var RCollection = require('lib/collection/rule');

    return Backbone.Model.extend({
        initialize: function() {
            this.rules     = new RCollection;
        },

        url: function() {
            return '/quickpoll/rest/poll/' + this.id;
        },

        fetchRules: function()
        {
            if (!this.id) {
                return this.rules;
            }

            var self = this;

            this.rules.setPollId(this.id);
            this.rules.fetch({
                success: function() {
                    self.trigger('rules::loaded');
                },
            });

            return this;
        },
    });
});

