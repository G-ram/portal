Meteor.startup(function () {
    if(Meteor.isClient){
      Tracker.autorun(function () {
          Meteor.subscribe("publicDatas");
          Session.set("datas",datas.findOne());
      });
    }
});
Router.configure({
  // we use the  appBody template to define the layout for the entire app
  layoutTemplate: 'appBody',

});
Router.route('/',{
  name:"home",
  render:"appBody"
});
