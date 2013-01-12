/**
 * license: MIT
 * author: Guillaume Luchet <guillaume@geelweb.org>
 */

define(function () {
    return Backbone.View.extend({
        initialize:function()
        {
            var self = this;

            this.model.on('rules::loaded', function() { self.initRules(); });
        },

        loadTemplate: function()
        {
            if (!this.template) {
                var self = this;

                $.ajax({
                    url: '/quickpoll/templates/poll/' + self.model.get('id'),
                    async: false,
                    success: function(template) {
                        self.template = _.template(template);
                        var html = self.template({
                        //    'poll_id': self.model.get('id'),
                        });
                        self.$el.html(html);
                        $('body').append(self.$el);

                        $("#quickpoll_dialog").dialog({
                            autoOpen: false,
                            modal: true,
                            buttons: {
                                Vote: function() {
                                    var form = $('#quickpoll_form'),
                                        action = form.attr('action'),
                                        data = $(form).serialize();

                                    $.ajax({
                                        url: action,
                                        data: data,
                                        type: 'POST',
                                        success: function(json, text) { console.log('json'); },
                                        error: function() { console.log('error'); }
                                    });

                                    $(this).dialog("close");
                                },
                                Cancel: function() {
                                    $(this).dialog("close");
                                }
                            },
                        });
                    }
                });
            }

            return this;
        },

        render: function()
        {
            this.loadTemplate();
            this.model.fetchRules();
            $("#quickpoll_dialog").dialog("open");
        },

        initRules: function()
        {
            var self = this;
            this.model.rules.forEach(function(rule) { self.initRule(rule); });
        },

        initRule: function(rule)
        {
            var self = this,
                question = rule.get('question'),
                choices = rule.get('choices'),
                display = rule.get('questions_displayed'),
                p = /^choice_[0-9]+_([0-9]+)$/;


            self.hideQuestions(display);

            $('input[name=choice_' + question + ']').change(function() {
                if(this.checked && _.indexOf(choices, parseInt(p.exec(this.id)[1])) != -1) {
                    self.showQuestions(display);
                } else {
                    self.hideQuestions(display);
                }
            });
        },

        showQuestion: function(id)
        {
            $('div#question_' + id).show();
        },

        showQuestions: function(ids)
        {
            var self = this;
            ids.forEach(function(id) { self.showQuestion(id); });
        },

        hideQuestion: function(id)
        {
            $('input[name=choice_' + id + ']').each(function() {
                if (this.checked) {
                    this.checked = false;
                    $(this).trigger('change');
                }
            });
            $('div#question_' + id).hide();
        },

        hideQuestions: function(ids)
        {
            var self = this;
            ids.forEach(function(id) { self.hideQuestion(id); });
        },
    });
});
