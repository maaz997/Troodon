import React from "react";
import axios from "axios";
import "antd/dist/antd.css";
import { PageHeader, Layout, Menu, Button, Divider } from "antd";
import "./Layout.css";
import MyData from "./MyData";
import ModelTrainingData from "./ModelTrainingData";
import OutputData from "./OutputData";

const LayoutComponent = () => {
  const { Header, Footer, Sider, Content } = Layout;
  const [currentNavSelected, setCurrentNavSelected] = React.useState("1");
  const [scriptCalled, setScriptCalled] = React.useState(false);
  const [scriptMessage, setScriptMessage] = React.useState(false);

  return (
    <Layout className="layout">
      <Header>
        <div className="logo" />
        <Menu theme="dark" mode="horizontal" defaultValue={currentNavSelected}>
          <Menu.Item
            key="1"
            onClick={() => {
              setCurrentNavSelected("1");
            }}
          >
            My Data
          </Menu.Item>
          <Menu.Item
            key="2"
            onClick={() => {
              setCurrentNavSelected("2");
            }}
          >
            Model Training Data
          </Menu.Item>
          <Menu.Item
            key="3"
            onClick={() => {
              setCurrentNavSelected("3");
            }}
          >
            Output
          </Menu.Item>
        </Menu>
      </Header>
      <Content style={{ padding: "0 50px" }}>
        <br />
        <Button
          onClick={() => {
            if (!scriptCalled) {
              axios.get("/script").then((resp) => {
                setScriptMessage(resp.data);
              });
            }
            setScriptCalled(true);
          }}
          danger
          disabled={scriptCalled}
        >
          Execute Scripts
        </Button>
        <Divider />
        <h3 style={{ color: "red" }}>{scriptMessage}</h3>
        <Divider />
        {currentNavSelected === "1" ? (
          <MyData />
        ) : currentNavSelected === "2" ? (
          <ModelTrainingData />
        ) : currentNavSelected === "3" ? (
          <OutputData />
        ) : null}
      </Content>
      <Footer style={{ textAlign: "center" }}></Footer>
    </Layout>
  );
};

export default LayoutComponent;
