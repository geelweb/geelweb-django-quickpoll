/**
 * license: MIT
 * author: Guillaume Luchet <guillaume@geelweb.org>
 */

define(function() {
    return Backbone.View.extend({
        template: _.template('<a href="#" class="open-poll"><%= label %></a>'),

        className: function()
        {
            var type = 'ribbon';
            if (this.options['type']) {
                type = this.options['type'];
            }

            return 'survey-' + type;
        },

        events: {
            "click .open-poll": "openPoll",
        },

        render: function()
        {
            var self = this;
            if($('.open-poll').length) {
                // manage elm with open-poll class outside the view
                $('.open-poll').click(function() {
                    self.openPoll();
                });
            }

            // get container
            var container = 'body';
            if (this.options['container']) {
                container = this.options['container'];
            }

            // get label
            var label = 'Survey';
            if (this.options['label']) {
                label = this.options['label'];
            }

            // render view
            this.$el.html(this.template({
                'label': label
            }));

            $(container).append(this.$el);
        },

        openPoll: function()
        {
            this.options['dialog'].render();
        },
    });
});
