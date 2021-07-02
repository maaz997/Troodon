import React from "react";
import socketIOClient from "socket.io-client";

const OutputData = () => {
  const [OutputDataResponse, setOutputDataResponse] = React.useState([]);

  React.useEffect(() => {
    const socket = socketIOClient("/");
    socket.on("HistoryData", (data) => {
      setOutputDataResponse(data);
    });
  }, []);

  return (
    <>
      <h1>Execution History Data</h1>
      <div className="site-layout-content">
        {OutputDataResponse !== undefined ? (
          <table>
            <tbody>
              {OutputDataResponse.map((subDivs, i) => (
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
        ) : null}{" "}
      </div>
    </>
  );
};
export default OutputData;
