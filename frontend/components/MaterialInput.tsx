import React, { useState, useEffect } from 'react';

type Item = { code: string; description: string; msrp_price: number };

type Props = {
  items: Item[];
  value: Item | null;
  onChange: (item: Item | null) => void;
};

const MaterialInput: React.FC<Props> = ({ items, value, onChange }) => {
  const [inputValue, setInputValue] = useState(value ? value.code : '');

  useEffect(() => {
    setInputValue(value ? value.code : '');
  }, [value]);

  return (
    <div>
      <label className="block mb-1 font-semibold">Material Code</label>
      <input
        className="w-full border rounded px-3 py-2 mb-2"
        list="material-codes"
        value={inputValue}
        onChange={e => {
          setInputValue(e.target.value);
          const found = items.find(i => i.code === e.target.value);
          onChange(found || null);
        }}
        placeholder="Start typing code or description..."
      />
      <datalist id="material-codes">
        {items.map(item => (
          <option key={item.code} value={item.code}>{`${item.code} - ${item.description}`}</option>
        ))}
      </datalist>
    </div>
  );
};

export default MaterialInput;
