import React from "react";
import socketIOClient from "socket.io-client";

const MyData = () => {
  const [myDataResponse, setMyDataResponse] = React.useState([]);

  React.useEffect(() => {
    const socket = socketIOClient("/");
    socket.on("ExecutionData", (data) => {
      setMyDataResponse(data);
    });
  }, []);

  return (
    <>
      <h1>Execution Data</h1>
      <div className="site-layout-content">
        {myDataResponse !== undefined ? (
          <table>
            <tbody>
              {myDataResponse.map((subDivs, i) => (
                <>
                  {subDivs.map((value, j) => (
                    <tr key={j}>
                      {value.map((innervalue, k) => (
                        <td key={k} style={{ padding: "10px" }}>
                          {innervalue}
                        </td>
                      ))}
                    </tr>
                  ))}
                </>
              ))}
            </tbody>
          </table>
        ) : null}
      </div>
    </>
  );
};
export default MyData;
