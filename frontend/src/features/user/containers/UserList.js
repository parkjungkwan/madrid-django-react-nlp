import React from 'react';
import Layout from 'features/common/components/Layout';
import styled from "styled-components";
import { UserListForm } from '..'


export default function UserList(){
  return(
    <Layout>
        <Main><UserListForm/></Main>
    </Layout>)
}

const Main = styled.div`
width: 500px;
margin: 0 auto;
text-decoration:none
text-align: center;
`