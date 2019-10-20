import React from 'react';
import * as routecall from '../utils/routecall';
import axios from 'axios';
import { Link } from 'react-router-dom';

import {
  List,
  ListItem,
  ListItemIcon,
  ListItemText,
  ListSubheader,
} from '@material-ui/core';

import RadioButtonCheckedIcon from '@material-ui/icons/RadioButtonChecked';
import RadioButtonUncheckedIcon from '@material-ui/icons/RadioButtonUnchecked';
import { url } from '../utils/constants';
import AuthContext from '../AuthContext';
import AddChannelDialog from './Channel/AddChannelDialog';

function ChannelList({ channel_id: curr_channel_id }) {
  const [myChannels, setMyChannels] = React.useState([]);
  const [allChannels, setAllChannels] = React.useState([]);

  const token = React.useContext(AuthContext);
  React.useEffect(() => {
    // fetch channels data
    const getMyChannels = () => {
      return routecall.get(`${url}/channels/list`, {
        params: {
          token,
        },
      });
    };

    const getAllChannels = () => {
      return routecall.get(`${url}/channels/listall`, {
        params: {
          token,
        },
      });
    };
    axios.all([getMyChannels(), getAllChannels()]).then(
      axios.spread((myChannelResponse, allChannelResponse) => {
        const myChannelData = myChannelResponse.data.channels;
        console.log(myChannelData);
        const allChannelData = allChannelResponse.data.channels;
        const filteredChannels = allChannelData.filter((channel) => {
          return (
            myChannelData.find((c) => c.channel_id === channel.channel_id) ===
            undefined
          );
        });
        console.log(filteredChannels);
        setMyChannels(myChannelData);
        setAllChannels(filteredChannels);
      })
    );
  }, []);

  return (
    <>
      <List
        subheader={
          <ListSubheader style={{ display: 'flex' }}>
            <span style={{ flex: 1 }}>My Channels</span>
            <AddChannelDialog />
          </ListSubheader>
        }
      >
        {myChannels.map(({ channel_id, name }, index) => (
          <ListItem
            button
            key={channel_id}
            component={Link}
            to={`/channel/${channel_id}`}
          >
            <ListItemIcon>
              {channel_id == curr_channel_id ? (
                <RadioButtonCheckedIcon />
              ) : (
                <RadioButtonUncheckedIcon />
              )}
            </ListItemIcon>
            <ListItemText primary={name} />
          </ListItem>
        ))}
      </List>
      <List subheader={<ListSubheader>Other Channels</ListSubheader>}>
        {allChannels.map(({ channel_id, name }, index) => (
          <ListItem
            button
            key={channel_id}
            component={Link}
            to={`/channel/${channel_id}`}
          >
            <ListItemIcon>
              {channel_id == curr_channel_id ? (
                <RadioButtonCheckedIcon />
              ) : (
                <RadioButtonUncheckedIcon />
              )}
            </ListItemIcon>
            <ListItemText primary={name} />
          </ListItem>
        ))}
      </List>
    </>
  );
}

export default ChannelList;
