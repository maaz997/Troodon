import { Divider } from "antd";
import React from "react";
import socketIOClient from "socket.io-client";

const ModelTraining = () => {
  const [ClassificationDataResponse, setClassificationDataResponse] =
    React.useState([]);
  const [SpeedupResponse, setSpeedupResponse] = React.useState([]);

  React.useEffect(() => {
    const socket = socketIOClient("/");
    socket.on("ModelData", (data) => {
      console.log("data", data);
      setClassificationDataResponse(data);
    });
  }, []);

  return (
    <>
      <h1>Classification Data</h1>
      <div className="site-layout-content">
        {ClassificationDataResponse !== undefined ? (
          <table>
            <tbody>
              {ClassificationDataResponse.map((subDivs, i) => (
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
      <Divider />
      {/* <h1>Speedup Data</h1>
      <div className="site-layout-content">
        {SpeedupResponse !== undefined ? (
          <table>
            <tbody>
              {SpeedupResponse.map((subDivs, i) => (
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
      </div> */}
    </>
  );
};
export default ModelTraining;
