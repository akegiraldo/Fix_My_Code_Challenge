var React = require('react');
var SinglePostActions = require('../actions/SinglePostActions');
var AuthorMixin = require('../mixins/AuthorMixin.jsx');
var createClass = require('create-react-class');

import PropTypes from 'prop-types';

var PostPreview = createClass({
//export default class PostPreview extends React.Component{
    contextTypes: {
        router: PropTypes.func
    },

    mixins: [AuthorMixin],

    loadPost : function(e){
        e.preventDefault();
        var self = this;
        self.context.router.transitionTo('/post/'+self.props.post.id+'/'+self.props.post.slug);
    },

    render : function() {
        return (
            <a href={'/post/' + this.props.post.id + '/' + this.props.post.slug} className="single-post" onClick={this.loadPost}>
                <div className="post-title">{this.props.post.title}</div>
                <div className="author-details">
                    {this.getAuthorDetails(this.props.post)}
                </div>
            </a>
        )
    }
});

module.exports = PostPreview;
