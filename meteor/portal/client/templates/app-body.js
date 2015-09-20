getRotatedRectBB = function(x,y,width,height,rAngle){
    var absCos=Math.abs(Math.cos(rAngle));
    var absSin=Math.abs(Math.sin(rAngle));
    var cx=x;
    var cy=y;
    var w=width*absCos+height*absSin;
    var h=width*absSin+height*absCos;
    return({cx:cx,cy:cy,width:w,height:h});
}
Template.appBody.onRendered(function () {
  this.autorun(function(){
    if(Session.get("datas")){
      var doc = Session.get("datas");
      x = 2*doc.x;
      y = 2*doc.y;
      theta = doc.theta;
      width=375;
      height=650;

      var canvas=$("#myCanvas")[0];
      var ctx=canvas.getContext("2d");

      var img=new Image();
      img.src="http://screen20.meteor.com/waldo.jpg";
      img.onload = start;
      function start(){
        var canvas1 = $("#tempCanvas1")[0];
        var ctx1=canvas1.getContext("2d");
        var canvas2=$("#tempCanvas2")[0];
        var ctx2=canvas2.getContext("2d");

        var rectBB=getRotatedRectBB(x,y,width,height,0);

        canvas1.width=canvas2.width=rectBB.width;
        canvas1.height=canvas2.height=rectBB.height;

        ctx1.drawImage(img,
           rectBB.cx-rectBB.width/2,
           rectBB.cy-rectBB.height/2,
           rectBB.width,
           rectBB.height,
           0,0,rectBB.width,rectBB.height
        );

        ctx2.translate(canvas1.width/2,canvas1.height/2);
        ctx2.rotate(0);
        ctx2.drawImage(canvas1,-canvas1.width/2,-canvas1.height/2);
        var offX=rectBB.width/2-width/2;
        var offY=rectBB.height/2-height/2;

        canvas.width=width;
        canvas.height=height;
        ctx.drawImage(canvas2,-offX,-offY);
      }
    }
  });
});
