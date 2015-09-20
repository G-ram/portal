var responseCodes = [{"code":401,"message":"Authentication required"},
					{"code":200,"message":"All good."},
					{"code":300,"message":"Not found."},
					{"code":305,"message":"Database error."}];
Router.route('/data/', {where: 'server'})
	.post(function(data){
		var res = this.response;
		res.end(JSON.stringify(responseCodes[1]));
	});
