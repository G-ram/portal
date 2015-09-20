Meteor.publish('publicDatas', function() {
  self = this;
  var userDatas = datas.find({}).observeChanges({
    added: function(id,fields){
      self.added("datas",id,fields);
    },
    changed: function(id, fields){
      self.changed("datas", id, fields);
    },
    removed:function(id){
      self.removed("datas",id);
    }
  });
  self.ready();
});
