import React, { Component } from 'react';
import axios from 'axios';

class Home extends Component {
  state = { data: [] }

  getData = () => {
    axios.get('/api/host/list/')
      .then((response) => {
        this.setState({data: response.data});
      })
      .catch((err) => console.log(err));
  }

  componentDidMount = () => {
    var intervalId = setInterval(this.getData, 1000);
    // store intervalId in the state so it can be accessed later:
    this.setState({intervalId: intervalId});
  }

  componentWillUnmount = () => {
   // use intervalId from the state to clear the interval
   clearInterval(this.state.intervalId);
  }

  render() {
    const { data } = this.state;
    return (
      <div>
        <center>
          <h1> Host List </h1>
        </center>
        {data.length === 0 && 'No Data received'}
        {
          data.map((item, index) => {
            return (
              <div key={index} style={{'padding':'20px', 'margin':'20px', 'border': '2px solid black'}}>
                <h3>{item.mac_addr} ({item.current_ip})</h3>
                {
                  item.parameters.map((param, key) => {
                    return <p key={key}>{param.oid} : <b>{param.value}</b></p>
                  })
                }
              </div>
            )
          }

          )
        }
      </div>
    );
  }
}

export default Home;
