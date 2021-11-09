import React from 'react';
import Layout from 'features/common/components/Layout';
import styled from "styled-components";
export default function Home(){
  return(
    <Layout>
        <Main><h1>시간이란...</h1>
        <p>내일 죽을 것처럼 오늘을 살고
            영원히 살 것처럼 내일을 꿈꾸어라.</p></Main>
    </Layout>)
}

const Main = styled.div`
width: 500px;
margin: 0 auto;
text-decoration:none
text-align: center;
`
