Router.configure({
  layoutTemplate: 'image',
  loadingTemplate: 'loading'
});
Router.route('/',{
  name:"main"
});
//On Before Actions
Router.onBeforeAction('loading');
