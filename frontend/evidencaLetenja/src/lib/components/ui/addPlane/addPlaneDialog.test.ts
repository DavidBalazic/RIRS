import { render, fireEvent, waitFor } from '@testing-library/svelte';
import AddPlaneDialog from './AddPlaneDialog.svelte';

test('opens dialog on clicking "Dodaj novo letalo"', async () => {
    const { getByText, queryByText } = render(AddPlaneDialog, {
        props: { onSave: vi.fn() },
    });

    expect(queryByText('Novo letalo')).not.toBeInTheDocument();

    const addButton = getByText('Dodaj novo letalo');
    await fireEvent.click(addButton);

    expect(queryByText('Novo letalo')).toBeInTheDocument();
    expect(queryByText('Tukaj lahko dodate novo letalo.')).toBeInTheDocument();
});

test('fills out all fields and saves the plane', async () => {
    const mockOnSave = vi.fn();
    const { getByText, getByLabelText, queryByText } = render(AddPlaneDialog, {
        props: { onSave: mockOnSave },
    });

    const addButton = getByText('Dodaj novo letalo');
    await fireEvent.click(addButton);

    const imeLetalaInput = getByLabelText('Ime letala');
    const tipInput = getByLabelText('Tip');
    const registrskaInput = getByLabelText('Registrska številka');
    const idFlightInput = getByLabelText('ID poleta');

    await fireEvent.input(imeLetalaInput, { target: { value: 'Letalo A' } });
    await fireEvent.input(tipInput, { target: { value: 'Jet' } });
    await fireEvent.input(registrskaInput, { target: { value: 'SLO-123' } });
    await fireEvent.input(idFlightInput, { target: { value: '42' } });

    const saveButton = getByText('Shrani');
    await fireEvent.click(saveButton);

    expect(mockOnSave).toHaveBeenCalledWith({
        ime_letala: 'Letalo A',
        tip: 'Jet',
        registrska_st: 'SLO-123',
        Polet_idPolet: 42,
    });
});

test("dialog is closed initially", () => {
    const { queryByText } = render(AddPlaneDialog, {
        props: { onSave: vi.fn() },
    });

    expect(queryByText("Novo letalo")).not.toBeInTheDocument();
});