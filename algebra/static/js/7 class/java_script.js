const canvas = document.querySelector("canvas")
const ctx = canvas.getContext("2d");
canvas.width = 700;
canvas.height = 400;
//ctx.transform(1, 0, 0, -1, 0, canvas.height)

const degreesToRadians = (n) => (n / 180) * Math.PI;
const radiansToDegrees = (n) => (n / Math.PI) * 180;



// Далее задаем начальные вершины для треугольника
const triangle = {
  vertices: [
    { x: (canvas.width / 3) , y: (canvas.height / 3) },
    { x: (canvas.width / 3) + 200, y: (canvas.height / 3) },
    { x: (canvas.width / 3) + 200, y: (canvas.height / 3) + 200 },
  ],
  selectedVertex: null,
};

//function resize(){
    //canvas.width = 400;
    //canvas.height = 400;
//}

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
  ctx.strokeStyle='rgba(100,150,185)';
  //ctx.closePath();
  ctx.stroke();

  for (let i = 0; i < triangle.vertices.length; i++) {

    ctx.beginPath();
    ctx.arc(triangle.vertices[i].x,triangle.vertices[i].y,8,0,2*Math.PI,false);
    ctx.strokeStyle='rgba(100,150,185,0.5)';
    ctx.fillStyle ='rgba(100,150,185,0.5)';
    ctx.fill();
    ctx.stroke();

    ctx.beginPath();
    ctx.arc(triangle.vertices[i].x,triangle.vertices[i].y,3,0,2*Math.PI,false);
    ctx.strokeStyle='blue';
    ctx.fillStyle ='blue';
    ctx.fill();
    ctx.stroke();
    
  }

    const coodsOfCentr = {
      sides: [
        { x: (triangle.vertices[0].x + triangle.vertices[1].x)/2, y:(triangle.vertices[0].y + triangle.vertices[1].y)/2},
        { x: (triangle.vertices[1].x + triangle.vertices[2].x)/2, y:(triangle.vertices[1].y + triangle.vertices[2].y)/2},
        { x: (triangle.vertices[2].x + triangle.vertices[0].x)/2, y:(triangle.vertices[2].y + triangle.vertices[0].y)/2},
      ]
    };

    function getAngles(x1,y1,x2,y2,x3,y3){
      var nx1 = x1 - x2;
      var ny1 = y1 - y2;
      var nx2 = x3 - x2;
      var ny2 = y3 - y2;

      console.log(nx1,ny1,nx2,ny2);
      
      var lineAngle1 = Math.atan2(ny1,nx1);
      var lineAngle2 = Math.atan2(ny2,nx2);
      console.log(lineAngle1, lineAngle2);
      
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
      ctx.strokeStyle='rgba(100,150,185,0.5)';
      ctx.fillStyle ='rgba(100,150,185,0.5)';
      ctx.fill();
      ctx.stroke();

      const mx = -Math.cos((lineAngle1 + lineAngle2) / 2) * 35 + x2;
      const my = -Math.sin((lineAngle1 + lineAngle2) / 2) * 35 + y2;

      // render the angle
      ctx.fillStyle = 'rgba(100,150,185)';
      ctx.font = "16px Georgia";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText((360-(lineAngle1 - lineAngle2) * (180 /Math.PI)).toFixed(0),mx,my)
    }

    function lenSides(x1,y1,x2,y2,side){
      vector = Math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
      ctx.fillText(Math.round(vector), coodsOfCentr.sides[side].x+15, coodsOfCentr.sides[side].y-20);
    }

    getAngles(triangle.vertices[1].x, triangle.vertices[1].y, triangle.vertices[0].x, triangle.vertices[0].y, triangle.vertices[2].x, triangle.vertices[2].y)
    getAngles(triangle.vertices[0].x, triangle.vertices[0].y, triangle.vertices[1].x, triangle.vertices[1].y, triangle.vertices[2].x, triangle.vertices[2].y)
    getAngles(triangle.vertices[1].x, triangle.vertices[1].y, triangle.vertices[2].x, triangle.vertices[2].y, triangle.vertices[0].x, triangle.vertices[0].y)
      
    lenSides(triangle.vertices[0].x,triangle.vertices[0].y,triangle.vertices[1].x,triangle.vertices[1].y,0);
    lenSides(triangle.vertices[1].x,triangle.vertices[1].y,triangle.vertices[2].x,triangle.vertices[2].y,1);
    lenSides(triangle.vertices[2].x,triangle.vertices[2].y,triangle.vertices[0].x,triangle.vertices[0].y,2);
        
    ctx.font = "21px Georgia";
    ctx.fillStyle = "Blue";
    ctx.fillText("A", triangle.vertices[0].x+10, triangle.vertices[0].y-10);
    ctx.fillText("B", triangle.vertices[1].x+10, triangle.vertices[1].y-10);
    ctx.fillText("C", triangle.vertices[2].x+10, triangle.vertices[2].y-10);
    getAngles();
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

    checkVertexSelection(x, y);
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