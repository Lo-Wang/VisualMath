const canvas = document.querySelector("canvas")
const ctx = canvas.getContext("2d");
canvas.width = 700;
canvas.height = 400;

const degreesToRadians = (n) => (n / 180) * Math.PI;
const radiansToDegrees = (n) => (n / Math.PI) * 180;

const alignment = 'center'; 
// Далее задаем начальные вершины для треугольника
const triangle = {
  vertices: [
    { x: (canvas.width / 2) - 150, y: (canvas.height / 3) + 200 },
    { x: (canvas.width / 2), y: (canvas.height / 3) },
    { x: (canvas.width / 2) + 150, y: (canvas.height / 3) + 200 },
  ],
  selectedVertex: 1,
};

function lineAtAngle(x1, y1, length, angle) {
  ctx.strokeStyle='rgba(68, 61, 62)';
  ctx.moveTo(x1, y1);
  ctx.lineTo(x1 + length * Math.cos(angle), y1 + length * Math.sin(angle));
  ctx.beginPath();
  ctx.arc(x1 + length * Math.cos(angle), y1 + length * Math.sin(angle),3,0,2*Math.PI,false);
  ctx.strokeStyle='#ff1176';
  ctx.fillStyle ='#ff1176';
  ctx.font = "21px Georgia";
  ctx.fill();
  //ctx.fillText("H", x1 + length * Math.cos(angle) + 10, y1 + length * Math.sin(angle) + 20);
  ctx.stroke();
  ctx.closePath();

}

// Функция отрисовки треугольника на холсте 
function drawTriangle() {
  ctx.lineWidth = 2;
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.textAlign = 'center';
  ctx.beginPath();
  ctx.moveTo(triangle.vertices[0].x, triangle.vertices[0].y);
  ctx.lineTo(triangle.vertices[1].x, triangle.vertices[1].y);
  ctx.lineTo(triangle.vertices[2].x, triangle.vertices[2].y);
  ctx.lineTo(triangle.vertices[0].x, triangle.vertices[0].y);
  ctx.moveTo(0, triangle.vertices[0].y);
  ctx.lineTo(canvas.width, triangle.vertices[0].y);
  ctx.strokeStyle='rgba(68, 61, 62)';
  vector = Math.sqrt((triangle.vertices[1].x-triangle.vertices[0].x)*(triangle.vertices[1].x-triangle.vertices[0].x)+(triangle.vertices[1].y-triangle.vertices[0].y)*(triangle.vertices[1].y-triangle.vertices[0].y))
  var mx1 = triangle.vertices[1].x - triangle.vertices[0].x;
  var my1 = triangle.vertices[1].y - triangle.vertices[0].y;
  var mx2 = triangle.vertices[2].x - triangle.vertices[0].x;
  var my2 = triangle.vertices[2].y - triangle.vertices[0].y;
      
  var mlineAngle1 = Math.atan2(my1,mx1);
  var mlineAngle2 = Math.atan2(my2,mx2);
  //console.log('угол', ((mlineAngle2 - mlineAngle1) * (180/Math.PI)))
  var len_H = vector*Math.sin((mlineAngle1 - mlineAngle2))
  //lineAtAngle(triangle.vertices[1].x, triangle.vertices[1].y, len_H, -Math.PI/2)
  //ctx.strokeStyle='rgba(100,150,185)';
  H_coord = {x:triangle.vertices[1].x + len_H * Math.cos(-Math.PI/2), y:triangle.vertices[1].y + len_H * Math.sin(-Math.PI/2)}
  ctx.moveTo(triangle.vertices[1].x, triangle.vertices[1].y);
  ctx.lineTo(H_coord.x, H_coord.y);
  ctx.stroke();
  ctx.closePath();

  ctx.beginPath();
  ctx.arc(H_coord.x, H_coord.y,3,0,2*Math.PI,false);
  ctx.strokeStyle='#ff1176';
  ctx.fillStyle ='#ff1176';
  ctx.font = "21px Georgia";
  ctx.fill();
  ctx.fillText("H", H_coord.x + 10, H_coord.y + 20);
  drawLabel(triangle.vertices[1], H_coord);
  ctx.closePath();
  ctx.stroke();
  ctx.beginPath();
  var vector1 = Math.sqrt((triangle.vertices[0].x-triangle.vertices[2].x)*(triangle.vertices[0].x-triangle.vertices[2].x)+(triangle.vertices[0].y-triangle.vertices[2].y)*(triangle.vertices[0].y-triangle.vertices[2].y))
  var Square = Math.abs(Math.round(0.5*vector1*len_H));
  console.log("Площадь", Square);
  if (Square % 10 == 3) {
    Square = Square;
    console.log("Площадь3", Square);
  }
  
  //ctx.fillText("S = 0,5 * AC * BH = " + (Square), 150, canvas.height - 20);
  ctx.closePath();

  for (let i = 0; i < triangle.vertices.length; i++) {

    ctx.beginPath();
    ctx.arc(triangle.vertices[i].x,triangle.vertices[i].y,8,0,2*Math.PI,false);
    ctx.strokeStyle='rgba(68, 61, 62,0.5)';
    ctx.fillStyle ='rgba(68, 61, 62,0.5)';
    ctx.fill();
    ctx.stroke();
    ctx.closePath();

    ctx.beginPath();
    ctx.arc(triangle.vertices[i].x,triangle.vertices[i].y,3,0,2*Math.PI,false);
    ctx.strokeStyle='#ff1176';
    ctx.fillStyle ='#ff1176';
    ctx.fill();
    ctx.stroke();
    ctx.closePath();
    
  }

    // const coodsOfCentr = {
    //   sides: [
    //     { x: (triangle.vertices[0].x + triangle.vertices[1].x)/2, y:(triangle.vertices[0].y + triangle.vertices[1].y)/2},
    //     { x: (triangle.vertices[1].x + triangle.vertices[2].x)/2, y:(triangle.vertices[1].y + triangle.vertices[2].y)/2},
    //     { x: (triangle.vertices[2].x + triangle.vertices[0].x)/2, y:(triangle.vertices[2].y + triangle.vertices[0].y)/2},
    //   ]
    // };

    function getAngles(x1,y1,x2,y2,x3,y3){
      var nx1 = x1 - x2;
      var ny1 = y1 - y2;
      var nx2 = x3 - x2;
      var ny2 = y3 - y2;
      
      var lineAngle1 = Math.atan2(ny1,nx1);
      var lineAngle2 = Math.atan2(ny2,nx2);
      
      // use cross product to find correct direction.
      if(nx1 * ny2 - ny1 * nx2 < 0){ // wrong way around swap direction
        const t = lineAngle2;
        lineAngle2 = lineAngle1;
        lineAngle1 = t;
      }
        
      // if angle 1 is behind then move ahead
      if(lineAngle1 < lineAngle2){
        lineAngle1 += Math.PI * 2;
      }
    
      ctx.beginPath();
      ctx.moveTo(x2,y2);
      ctx.arc(x2,y2,20,lineAngle1,lineAngle2,false);
      ctx.strokeStyle='rgba(68, 61, 62,0.5)';
      ctx.fillStyle ='rgba(68, 61, 62,0.5)';
      ctx.fill();
      ctx.stroke();

      const mx = -Math.cos((lineAngle1 + lineAngle2) / 2) * 35 + x2;
      const my = -Math.sin((lineAngle1 + lineAngle2) / 2) * 35 + y2;

      // render the angle
      ctx.fillStyle = 'rgba(68, 61, 62)';
      ctx.font = "16px Georgia";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText((360-(lineAngle1 - lineAngle2) * (180 /Math.PI)).toFixed(0),mx,my)
      ctx.closePath();
    }

    // function lenSides(x1,y1,x2,y2,side){
    //   vector = Math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
    //   ctx.fillText(Math.round(vector), coodsOfCentr.sides[side].x+15, coodsOfCentr.sides[side].y-20);
    // }


    function drawLabel(g, h){
      var padding = 20;
      var dx = g.x - h.x;
      var dy = g.y - h.y; 
      var len = Math.sqrt(dx*dx+dy*dy);
      let angle1 = Math.atan2(dy,dx);
      if (angle1 < -Math.PI/2 || angle1  > Math.PI/2){
        var w = h;
        h = g;
        g = w;
        dx *= -1;
        dy *= -1;
        //selectedVertex = Math.abs(selectedVertex-1)
        angle1 -= Math.PI;
      }
    
      let t0, pad;
      t0 = h;
      pad = 1/2;
    
      ctx.save();
      ctx.beginPath();
      ctx.textAlign = alignment;
      ctx.translate(t0.x+dx*pad,t0.y+dy*pad);
      ctx.rotate(angle1);
      ctx.font = '16px  Arial';
      ctx.strokeStyle ='rgba(68, 61, 62)';
      ctx.fillStyle ='rgba(68, 61, 62)';
      vector = Math.sqrt((h.x-g.x)*(h.x-g.x)+(h.y-g.y)*(h.y-g.y))
      //console.log(vector)
      ctx.fillText(Math.round(vector),5,-5);
      ctx.fill();
      ctx.stroke();
      ctx.closePath();
      ctx.restore();
    
    }

    getAngles(triangle.vertices[1].x, triangle.vertices[1].y, triangle.vertices[0].x, triangle.vertices[0].y, triangle.vertices[2].x, triangle.vertices[2].y)
    getAngles(triangle.vertices[0].x, triangle.vertices[0].y, triangle.vertices[1].x, triangle.vertices[1].y, triangle.vertices[2].x, triangle.vertices[2].y)
    getAngles(triangle.vertices[1].x, triangle.vertices[1].y, triangle.vertices[2].x, triangle.vertices[2].y, triangle.vertices[0].x, triangle.vertices[0].y)
      

    drawLabel(triangle.vertices[0], triangle.vertices[1])
    drawLabel(triangle.vertices[1], triangle.vertices[2])
    drawLabel(triangle.vertices[2], triangle.vertices[0])

    // lenSides(triangle.vertices[0].x,triangle.vertices[0].y,triangle.vertices[1].x,triangle.vertices[1].y,0);
    // lenSides(triangle.vertices[1].x,triangle.vertices[1].y,triangle.vertices[2].x,triangle.vertices[2].y,1);
    // lenSides(triangle.vertices[2].x,triangle.vertices[2].y,triangle.vertices[0].x,triangle.vertices[0].y,2);
        
    ctx.font = "21px Georgia";
    ctx.fillStyle = '#ff1176';
    ctx.fillText("A", triangle.vertices[0].x-10, triangle.vertices[0].y-10);
    ctx.fillText("B", triangle.vertices[1].x+10, triangle.vertices[1].y-10);
    ctx.fillText("C", triangle.vertices[2].x+10, triangle.vertices[2].y-10);
    //getAngles();
}
  
  // Проверяет насколько близко курсор мыши
  function checkVertexSelection(x, y) {
    for (let i = 0; i < triangle.vertices.length; i++) {
      const vertex = triangle.vertices[i];
      const distance = Math.sqrt((x - vertex.x) ** 2 + (y - vertex.y) ** 2);
      if (distance < 5) {
        triangle.selectedVertex = i;
        return;
      }
    }
    triangle.selectedVertex = null;
  }

  // Добавляем реакцию на клик мыши по холсту
  canvas.addEventListener("mousedown", (e) => {
    const x = e.clientX - canvas.getBoundingClientRect().left;
    const y = e.clientY - canvas.getBoundingClientRect().top;

    //checkVertexSelection(x, y);
      // Следим за перемещениями мыши и другими действиями
      // в частности за перемещением вершины при удержании лкм
      // и завершением перемещения 
    canvas.addEventListener("mousemove", moveVertex);
    canvas.addEventListener("mouseup", () => {
      canvas.removeEventListener("mousemove", moveVertex);
    });
  });
  // Обрабатываем перемещение вершины
  function moveVertex(e) {
    const x = e.clientX - canvas.getBoundingClientRect().left;
    const y = e.clientY - canvas.getBoundingClientRect().top;

    if (triangle.selectedVertex !== null) {
      triangle.vertices[triangle.selectedVertex].x = x;
      triangle.vertices[triangle.selectedVertex].y = y;
      drawTriangle();
    }
  }
  // для начальной отрисовки треугольника
  drawTriangle();