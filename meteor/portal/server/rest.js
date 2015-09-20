var responseCodes = [{"code":401,"message":"Authentication required"},
					{"code":200,"message":"All good."},
					{"code":300,"message":"Not found."},
					{"code":305,"message":"Database error."}];
Meteor.startup(function(){
	datas.insert({"x": 0,"y": 0,"theta": 0});
});
Router.route('/data/', {where: 'server'})
	.post(function(data){
		var res = this.response;
		datas.update({},{"x": ""+data.body.x,"y": ""+data.body.y,"theta": ""+data.body.theta},
		function(error){
			if(error){
				res.end(JSON.stringify(responseCodes[3]));
			}
		});
		res.end(JSON.stringify(responseCodes[1]));
	});
