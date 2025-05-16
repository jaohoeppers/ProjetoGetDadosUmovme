import React, { useState } from 'react';
import { Container, Paper, Typography, TextField, Button, Box } from '@mui/material';

interface Props {
  teste: string;
}

const StyledInterface: React.FC<Props> = ({ teste }) => {
  const [formData, setFormData] = useState({
    mesesAnteriores: '',
    ultimoDia: '',
    usuario: '',
    senha: '',
    aba: ''
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  return (
    <Container maxWidth="sm" sx={{ mt: 8 }}>
      <Paper elevation={4} sx={{ p: 4, borderRadius: 3 }}>
        <Typography variant="h5" gutterBottom align="center">
          Buscar Dados
        </Typography>
        <Box component="form" sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
          <TextField
            label="Número de meses anteriores"
            name="mesesAnteriores"
            type="number"
            variant="outlined"
            value={formData.mesesAnteriores}
            onChange={handleChange}
            fullWidth
            required
          />
          <TextField
            label="Último dia do mês escolhido"
            name="ultimoDia"
            type="number"
            variant="outlined"
            value={formData.ultimoDia}
            onChange={handleChange}
            fullWidth
            required
            InputLabelProps={{ shrink: true }}
          />
          <TextField
            label="Usuário"
            name="usuario"
            variant="outlined"
            value={formData.usuario}
            onChange={handleChange}
            fullWidth
            required
          />
          <TextField
            label="Senha"
            name="senha"
            type="password"
            variant="outlined"
            value={formData.senha}
            onChange={handleChange}
            fullWidth
            required
          />
          <TextField
            label="Aba da planilha que os ambientes estão"
            name="abaPlanilha"
            type="text"
            variant="outlined"
            value={formData.aba}
            onChange={handleChange}
            fullWidth
            required
          />
          <Button 
            type="submit" 
            onClick={() => handleSave(formData)} 
            variant="contained" 
            color="primary"
            size="large"
          >
            Buscar
          </Button>
        </Box>
      </Paper>
    </Container>
  );
};

const handleSave = async (data: {
  mesesAnteriores: string;
  ultimoDia: string;
  usuario: string;
  senha: string;
}) => {
  await fetch('http://localhost:3001/save-data', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
};


export default StyledInterface;
