var responseCodes = [{"code":401,"message":"Authentication required"},
					{"code":200,"message":"All good."},
					{"code":300,"message":"Not found."},
					{"code":305,"message":"Database error."}];
Router.route('/data/', {where: 'server'})
	.post(function(data){
		var res = this.response;
		data.update({"_id":"55fe3a0dce7a2f336ad242e0"},{"x":this.params.x,"y":this.params.y,"theta":this.params.theta},
		function(error){
			if(error){
				res.end(JSON.stringify(responseCodes[3]));
			}
		});
		res.end(JSON.stringify(responseCodes[1]));
	});
