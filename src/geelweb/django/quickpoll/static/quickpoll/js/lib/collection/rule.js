/**
 * license: MIT
 * author: Guillaume Luchet <guillaume@geelweb.org>
 */

define(function (require){
    var model = require('lib/model/rule');

    return Backbone.Collection.extend({
        model: model,

        setPollId: function(poll_id)
        {
            this.poll_id = poll_id;
            return this;
        },

        url: function()
        {
            return '/quickpoll/rest/poll/' + this.poll_id + '/rules'
        },
    });
});

