import { render, fireEvent } from '@testing-library/svelte';
import AddFlightDialog from './addFlightDialog.svelte';

test('opens and closes dialog', async () => {
  const { getByText, queryByText } = render(AddFlightDialog, {
    props: { onSave: vi.fn() },
  });

  expect(queryByText('Nov polet')).not.toBeInTheDocument();

  const openButton = getByText('Dodaj');
  await fireEvent.click(openButton);

  expect(getByText('Nov polet')).toBeInTheDocument();
});

test('closes dialog on save', async () => {
    const mockOnSave = vi.fn();
    const { getByText, queryByText, getByLabelText } = render(AddFlightDialog, {
      props: { onSave: mockOnSave },
    });
  
    const openButton = getByText('Dodaj');
    await fireEvent.click(openButton);
  
    expect(getByText('Nov polet')).toBeInTheDocument();
  
    const idPilotaInput = getByLabelText('ID Pilota');
    await fireEvent.input(idPilotaInput, { target: { value: '123' } });
  
    const saveButton = getByText('Shrani');
    await fireEvent.click(saveButton);
  
    expect(mockOnSave).toHaveBeenCalledWith({
      cas_vzleta: '',
      cas_pristanka: '',
      Pilot_idPilot: 123,
    });
  });