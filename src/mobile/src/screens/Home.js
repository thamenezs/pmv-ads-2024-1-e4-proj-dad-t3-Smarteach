import { useState } from 'react';
import { BottomNavigation } from 'react-native-paper';

import Turmas from '../screens/Turmas';
import Mural from '../screens/Mural';
import Usuarios from '../screens/Usuarios';
import Configuracoes from '../screens/Configuracoes';

const Home = () => {
  const [index, setIndex] = useState(0);

  const [routes] = useState([
    { key: 'turmas', title: 'Turmas', focusedIcon: 'home' },
    { key: 'mural', title: 'Mural', focusedIcon: 'calendar' },
    { key: 'usuarios', title: 'Usuarios', focusedIcon: 'account' },
    { key: 'configuracoes', title: 'Configuracoes', focusedIcon: 'cog' },
  ]);

  const renderScene = BottomNavigation.SceneMap({
    turmas: Turmas,
    mural: Mural,
    usuarios: Usuarios,
    configuracoes: Configuracoes,
  });

  return (
    <BottomNavigation
      activeColor='white'
      inactiveColor='white'
      barStyle={{ backgroundColor: `#004AAD` }}
      navigationState={{ index, routes }}
      onIndexChange={setIndex}
      renderScene={renderScene}
    />
  )
}

export default Home;