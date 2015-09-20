Meteor.subscribe("data")
Template.image.helpers({
  canvasUpdate: function(){
    var doc = Data.findOne();
    x = doc.x;
    y = doc.y;
    theta = doc.theta;
	},
});
