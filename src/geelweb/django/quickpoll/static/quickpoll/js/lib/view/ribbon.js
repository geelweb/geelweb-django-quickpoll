/**
 * license: MIT
 * author: Guillaume Luchet <guillaume@geelweb.org>
 */

define(function() {
    return Backbone.View.extend({
        template: _.template('<a href="#" class="open-poll"><%= label %></a>'),

        attributes: {
            'class': 'survey-ribbon',
        },

        events: {
            "click .open-poll": "openPoll",
        },

        render: function()
        {
            this.$el.html(this.template({
                'label': 'Sondage', // TODO I18N
            }));

            $('body').append(this.$el);
        },

        openPoll: function()
        {
            this.options['dialog'].render();
        },
    });
});
