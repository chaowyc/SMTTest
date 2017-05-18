/**
 * Created by chaowyc on 17-5-2.
 */

g = new Dygraph(
    document.getElementById("graph"),
    "X,Y,Z\n" +
    "1,0,3\n" +
    "2,2,6\n" +
    "3,4,8\n" +
    "4,6,9\n" +
    "5,8,9\n" +
    "6,10,8\n" +
    "7,12,6\n" +
    "8,14,3\n",
    {
        legend: 'always',
        animatedZooms: true,
        title: 'dygraphs chart template'
    }
);