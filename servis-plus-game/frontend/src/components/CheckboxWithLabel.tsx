interface Props {
  text: string;
  id: string;
  className: string;
  onChange?: (event: React.ChangeEvent<HTMLInputElement>) => void;
}

function CheckboxWithLabel({ text, id, className, onChange }: Props) {
  return (
    <div>
      <input
        type="checkbox"
        id={id}
        className={className}
        onChange={onChange}
      />
      <label htmlFor={id}>{text}</label>
    </div>
  );
}

CheckboxWithLabel.defaultProps = {
  text: "",
  id: "",
  className: "",
  onChange: undefined,
};

export default CheckboxWithLabel;
